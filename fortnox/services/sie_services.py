class SIEService(object):
    """
    :class:`fortnox.SIEService` is used by :class:`fortnox.Client` to make
    actions related to SIE resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for SIE to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = []
    SERVICE = "SIE"

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
        Retrieve all SIE

        Returns all SIE available to the Company, according to the parameters provided

        :calls: ``get /sie``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of SIE.
        :rtype: list
        """

        _, _, files = self.http_client.get("/sie", params=params)
        return files

    def retrieve(self, type):
        """
        Retrieve a single SIE

        Returns a single SIE according to the unique SIE ID provided
        If the specified SIE does not exist, this query returns an error

        :calls: ``get /sie/{type}``
        :param int id: Unique identifier of a SIE.
        :return: Dictionary that support attriubte-style access and represent SIE resource.
        :rtype: dict
        """
        _, _, file = self.http_client.get("/sie/{type}".format(type=type))
        return file
