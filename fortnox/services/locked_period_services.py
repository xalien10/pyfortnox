class LockedPeriodService(object):
    """
    :class:`fortnox.LockedPeriodService` is used by :class:`fortnox.Client` to make
    actions related to LockedPeriod resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for LockedPeriod to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = []
    SERVICE = "LockedPeriod"

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
        Retrieve all LockedPeriod

        Returns all LockedPeriod available to the Company, according to the parameters provided

        :calls: ``get /settings/lockedperiod``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of LockedPeriod.
        :rtype: list
        """

        _, _, locked_periods = self.http_client.get("/settings/lockedperiod", params=params)
        return locked_periods
