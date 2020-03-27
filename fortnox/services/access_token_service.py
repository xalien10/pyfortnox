class AccessTokenService(object):
    """
    :class:`fortnox.AccessTokenService` is used by :class:`fortnox.Client` to obtain
    access token for using in other operations.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for CompanySettings to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = []
    SERVICE = "AccessToken"

    def __init__(self, http_client):
        """
        :param :class:`fortnox.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client

    def access_token(self, **params):
        """
        Retrieve Access-Token

        Returns Access-Token which will be used in all endpoints in fortnox

        :calls: ``get /``
        :param dict params: (optional) Search options.
        :return: AccessToken.
        :rtype: munch object
        """
        params['service'] = self.SERVICE
        _, _, access_token = self.http_client.get("/", params=params)
        return access_token
