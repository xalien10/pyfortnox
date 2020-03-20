class CompanySettingsService(object):
    """
    :class:`fortnox.CompanySettingsService` is used by :class:`fortnox.Client` to make
    actions related to CompanySettings resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for CompanySettings to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = []
    SERVICE = "CompanySettings"

    def __init__(self, http_client):
        """
        :param :class:`fortnox.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client

    def info(self, **params):
        """
        Retrieve CompanySettings

        Returns all information available to the CompanySettings, according to the parameters provided

        :calls: ``get /settings/company``
        :param dict params: (optional) Search options.
        :return: dictionaries that support attriubte-style access, which represent collection of CompanySettings.
        :rtype: munch object
        """

        _, _, company_settings = self.http_client.get("/settings/company", params=params)
        return company_settings
