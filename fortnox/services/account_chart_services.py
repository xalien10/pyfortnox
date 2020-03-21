class AccountChartsService(object):
    """
    :class:`fortnox.AccountChartsService` is used by :class:`fortnox.Client` to make
    actions related to Account Charts resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for AccountCharts to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = []
    SERVICE = "AccountChart"

    def __init__(self, http_client):
        """
        :param :class:`fortnox.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client

    def list(self, **params):
        """
        Retrieve all Account Charts

        Returns all Account Chart available to the Company, according to the parameters provided

        :calls: ``get /accountcharts``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Account Charts.
        :rtype: list
        """

        _, _, account_charts = self.http_client.get("/accountcharts", params=params)
        return account_charts
