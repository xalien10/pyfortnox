class CurrencyService(object):
    """
    :class:`fortnox.CurrencyService` is used by :class:`fortnox.Client` to make
    actions related to Currency resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for currencies to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Code', 'Description']
    SERVICE = "Currency"

    def __init__(self, http_client):
        """
        :param :class:`fortnox.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client

    def list(self, code=None, **params):
        """
        Retrieve all <specific-service>

        Returns all <specific-service> available to the Company, according to the parameters provided

        :calls: ``get /currencies``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Customers.
        :rtype: list
        """
        if code:
            url = "/currencies/{code}".format(code=code)
        else:
            url = "/currencies"
        _, _, currencies = self.http_client.get(url, params=params)
        return currencies

    def retrieve(self, code):
        """
        Retrieve a single <specific-service>

        Returns a single <specific-service> according to the unique <specific-service> ID provided
        If the specified <specific-service> does not exist, this query returns an error

        :calls: ``get /currencies/{code}``
        :param int id: Unique identifier of a <specific-service>.
        :return: Dictionary that support attriubte-style access and represent <specific-service> resource.
        :rtype: dict
        """
        _, _, currency = self.http_client.get("/currencies/{code}".format(code=code))
        return currency

    def create(self, *args, **kwargs):
        """
        Create a <specific-service>

        Creates a new customer
        **Notice** the customer's name **must** be unique within the scope of the resource_type

        :calls: ``post /currencies``
        :param tuple *args: (optional) Single object representing <specific-service> resource.
        :param dict **kwargs: (optional) Customer attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Customer resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Currency are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, currency = self.http_client.post("/currencies", body=attributes)
        return currency

    def update(self, code, *args, **kwargs):
        """
        Update a <specific-service>

        Updates a <specific-service>'s information
        If the specified <specific-service> does not exist, this query will return an error
        **Notice** if you want to update a <specific-service>, you **must** make sure the <specific-service>'s name is unique within the scope of the specified resource

        :calls: ``put /currencies/{code}``
        :param int id: Unique identifier of a <specific-service>.
        :param tuple *args: (optional) Single object representing <specific-service> resource which attributes should be updated.
        :param dict **kwargs: (optional) <specific-service> attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated <specific-service> resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Currency are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, currency = self.http_client.put("/currencies/{code}".format(code=code), body=attributes)
        return currency

    def destroy(self, code):
        """
        Delete a <specific-service>

        Deletes an existing <specific-service>
        If the specified <specific-service> is assigned to any resource, we will remove this <specific-service> from all such resources
        If the specified <specific-service> does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /currencies/{code}``
        :param int id: Unique identifier of a <specific-service>.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/currencies/{code}".format(code=code))
        return status_code == 204
