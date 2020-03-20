from munch import munchify


class ConfigurationError(Exception):
    """
    Exception raised in case of invalid client configuration e.g. no access token provided,
    invalid access token, invalid base url etc.
    """
    pass


class RateLimitError(Exception):
    """
    Exception raised when the rate limit was exceeded.
    """
    pass


class BaseError(Exception):
    """
    This is the base class for all the errors returned by Fortnox backend servers.

    Classes derived from this class:
    * :class:`RequestError <RequestError>`
    * :class:`ResourceError <ResourceError>`
    * :class:`ServerError <ServerError>`

    :attribute int http_status: Http status code.
    :attribute str code: Request unique identifier.
    :attribute list errors: List of :class:`Munch <munch.Munch>` objects repsenting returned errors.

    Each error object has following attributes:
    :attribute str code: The error code.
    :attribute str message: Human redable error description.
    :attribute str details: (optional) Detailed description.
    :attribute str resource: (optional) Resource name the error relates to.
    :attribute str field: (optional) Field name of the resource the error relates to, in the JSON pointer format.
    """

    def __init__(self, http_status, errors_payload):
        """
        :param int http_status: Http status code.
        :param dict errors_payload: Json decoded payload from the errors response.
        """
        self.http_status = http_status
        self.errors = munchify(errors_payload['ErrorInformation'])

        try:
            error_code = self.errors.Code
        except:
            error_code = self.errors.code

        self.code = error_code

        try:
            error_message = self.errors.Message
        except:
            error_message = self.errors.message

        message = "\n".join([str(error_message)])
        super(BaseError, self).__init__(message)


class RequestError(BaseError):
    """
    Exception raised if the request was invalid e.g. unknown query parameter,
    invalid request's body envelope etc.
    """
    pass


class ResourceError(BaseError):
    """
    Exception raised in case of any resource related error.
    """
    pass


class ServerError(BaseError):
    """
    Exception raised if Fortnox's servers encountered an unexpected condition.
    """
    pass
