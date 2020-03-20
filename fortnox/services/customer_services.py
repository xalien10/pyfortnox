class CustomerService(object):
    """
    :class:`fortnox.CustomerService` is used by :class:`fortnox.Client` to make
    actions related to Note resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Customer to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['content', 'resource_id', 'resource_type']

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
        Retrieve all customers

        Returns all notes available to the user, according to the parameters provided

        :calls: ``get /customers``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Customers.
        :rtype: list
        """

        _, _, customers = self.http_client.get("/customers", params=params)
        return customers
