class CompanyInformationService(object):
    """
    :class:`fortnox.CompanyInformationService` is used by :class:`fortnox.Client` to make
    actions related to Company Information resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for CompanyInformation to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = []
    SERVICE = "CompanyInformation"

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
        Retrieve Company Information

        Returns Company Information available to the Company, according to the parameters provided

        :calls: ``get /companyinformation``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Company.
        :rtype: dict object
        """

        _, _, company = self.http_client.get("/companyinformation", params=params)
        return company
