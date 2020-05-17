import json
from decimal import Decimal

import requests
from munch import munchify
from requests_toolbelt import MultipartEncoder

from fortnox.errors import ResourceError, RateLimitError, RequestError, ServerError


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)


class HttpClient(object):
    """
    Wrapper over :module:`requests` that understands Base CRM envelope, encoding and decoding schema.
    """

    """
    Supported REST API version prefix.
    """
    API_VERSION = '/3'

    def __init__(self, config):
        """
        :param :class:`fortnox.Configuration` config: Base CRM client configuration.
        """

        self.config = config

        # if self.config.verbose:
        #     self.enable_logging()

    def get(self, url, params=None, **kwargs):
        """
        Send a GET request.

        :param str url: Sub URL for the request. You MUST not specify neither base url nor api version prefix.
        :param dict params: (optional) Dictionary of query parameters.
        :param dict **kwargs: (optional) Other parameters which are directly passed to :func:`requests.request`.
        :return: Tuple of three elements: (http status code, headers, response - either parsed json or plain text)
        :rtype: tuple
        """

        return self.request('get', url, params=params, **kwargs)

    def post(self, url, body=None, **kwargs):
        """
        Send a POST request.

        :param str url: Sub URL for the request. You MUST not specify neither base url nor api version prefix.
        :param dict body: (optional) Dictionary of body attributes that will be wrapped with envelope and json encoded.
        :param dict **kwargs: (optional) Other parameters which are directly passed to :func:`requests.request`.
        :return: Tuple of three elements: (http status code, headers, response - either parsed json or plain text)
        :rtype: tuple
        """

        return self.request('post', url, body=body, **kwargs)

    def put(self, url, body=None, **kwargs):
        """
        Send a PUT request.

        :param str url: Sub URL for the request. You MUST not specify neither base url nor api version prefix.
        :param dict body: (optional) Dictionary of body attributes that will be wrapped with envelope and json encoded.
        :param dict **kwargs: (optional) Other parameters which are directly passed to :func:`requests.request`.
        :return: Tuple of three elements: (http status code, headers, response - either parsed json or plain text)
        :rtype: tuple
        """

        return self.request('put', url, body=body, **kwargs)

    def delete(self, url, params=None, **kwargs):
        """
        Send a DELETE request.

        :param str url: Sub URL for the request. You MUST not specify neither base url nor api version prefix.
        :param dict params: (optional) Dictionary of query parameters.
        :param dict **kwargs: (optional) Other parameters which are directly passed to :func:`requests.request`.
        :return: Tuple of three elements: (http status code, headers, response - either parsed json or plain text)
        :rtype: tuple
        """

        return self.request('delete', url, params=params, **kwargs)

    def request(self, method, url, params=None, body=None, **kwargs):
        """
        Send an HTTP request.

        The :param:`params` will be properly encoded, as well as :param:`body` which
        will be wrapped with envelope the API expects and json encoded.

        When you get a response the method will try to json decode the response,
        if the media type represents json, unwrap the envelope and munchify what has left,
        for JavaScript like access.

        :param str url: Sub URL for the request. You MUST not specify neither base url nor api version prefix.
        :param dict params: (optional) Dictionary of query parameters.
        :param dict body: (optional) Dictionary of body attributes that will be wrapped with envelope and json encoded.
        :param dict **kwargs: (optional) Other parameters which are directly passed to :func:`requests.request`.
        :raises RequestError: if authentication failed, invalid query parameter etc.
        :raises RateLimitError: if rate limit exceeded.
        :raises ResourceError: if requests payload included invalid attributes or were missing.
        :raises ServerError: if Base CRM backend servers encounterered an unexpected condition.
        :return: Tuple of three elements: (http status code, headers, response - either parsed json or plain text)
        :rtype: tuple

        :Keyword Arguments:
            * :param dict headers: (optional) Dictionary of headers. Default: ``{}``.
            * :param bool raw: (optional) Whether to wrap and uwrap the envelope. Default: ``False``.
        """

        url = "{base_url}{version}{resource}".format(base_url=self.config.base_url,
                                                     version=self.API_VERSION,
                                                     resource=url)

        need_to_obtain_access_token = False
        try:
            if 'service' in params.keys():
                key = params.get('service')
                if key == "AccessToken":
                    need_to_obtain_access_token = True
                    params.pop('service')
        except:
            pass

        if not need_to_obtain_access_token:
            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Access-Token': "{access_token}".format(access_token=self.config.access_token),
                'Client-Secret': "{client_secret}".format(client_secret=self.config.client_secret)
            }
        else:
            headers = {
                'Authorization-Code': "{authorization_code}".format(authorization_code=self.config.authorization_code),
                'Client-Secret': "{client_secret}".format(client_secret=self.config.client_secret)
            }

        user_headers = {}
        if 'headers' in kwargs and isinstance(kwargs['headers'], dict):
            user_headers = kwargs['headers']

        headers.update(user_headers)

        raw = bool(kwargs['raw']) if 'raw' in kwargs else False

        if body is not None:
            # payload = body if raw else self.wrap_envelope(body)
            if 'file' in body:
                # if endpoint contains file
                sent_file = body.get('file')
                file_name = body.pop('file_name')
                file = MultipartEncoder(
                    fields={
                        'file': (file_name, sent_file, 'application/octet-stream')
                    }
                )
                headers['Content-Type'] = file.content_type
                headers['Accept'] = '*/*'
                body = file
            else:
                body = json.dumps(self.wrap_envelope(body), cls=DecimalEncoder)
        resp = requests.request(method, url,
                                params=params,
                                data=body,
                                headers=headers,
                                timeout=float(self.config.timeout),
                                )

        if not (200 <= resp.status_code < 300):
            self.handle_error_response(resp)

        if 'Content-Type' in resp.headers and 'json' in resp.headers['Content-Type']:
            resp_body = munchify(resp.json()) if raw else self.unwrap_envelope(resp.json())
        else:
            resp_body = resp.content

        return (resp.status_code, resp.headers, resp_body)

    def handle_error_response(self, resp):
        try:
            errors = resp.json()
        except ValueError:
            errors = {'errors': [], 'meta': {'logref': ''}}

        resp_code = resp.status_code
        if resp_code == 422:
            raise ResourceError(resp_code, errors)
        elif resp_code == 429:
            raise RateLimitError()
        elif 400 <= resp_code < 500:
            raise RequestError(resp_code, errors)
        elif 500 <= resp_code < 600:
            raise ServerError(resp_code, errors)
        else:
            raise Exception('Unknown HTTP error response')

    @staticmethod
    def wrap_envelope(body):
        key = 'data'
        if 'service' in body.keys():
            key = body.get('service')
            body.pop('service')
        return {key: body}

    @staticmethod
    def unwrap_envelope(body):
        if body is '' or body is None:
            # Sometimes response body returns nothing from Fortnox API
            return True
        keys = [key for key in body.keys()]
        return [munchify(item) for item in body.get(keys[1])] if len(keys) > 1 else munchify(body.get(keys[0]))

    def enable_logging(self):
        import logging
        try:
            import http.client as http_client
        except ImportError:
            # Python 2
            import httplib as http_client
        http_client.HTTPConnection.debuglevel = 1

        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True
