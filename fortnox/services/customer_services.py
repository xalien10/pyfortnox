class CustomerService(object):
    """
    :class:`fortnox.CustomerService` is used by :class:`fortnox.Client` to make
    actions related to Customer resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Customer to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Name']
    SERVICE = "Customer"

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

        Returns all Customers available to the Company, according to the parameters provided

        :calls: ``get /customers``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Customers.
        :rtype: list
        """

        _, _, customers = self.http_client.get("/customers", params=params)
        return customers

    def retrieve(self, id):
        """
        Retrieve a single customer

        Returns a single Customer according to the unique Customer ID provided
        If the specified Customer does not exist, this query returns an error

        :calls: ``get /customers/{id}``
        :param int id: Unique identifier of a Customer.
        :return: Dictionary that support attriubte-style access and represent User resource.
        :rtype: dict
        """
        _, _, customer = self.http_client.get("/customers/{id}".format(id=id))
        return customer

    def create(self, *args, **kwargs):
        """
        Create a customer

        Creates a new customer
        **Notice** the customer's name **must** be unique within the scope of the resource_type

        :calls: ``post /customers``
        :param tuple *args: (optional) Single object representing Customer resource.
        :param dict **kwargs: (optional) Customer attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Customer resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Customer are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items() if k in self.OPTS_KEYS_TO_PERSIST)
        attributes.update({'service': self.SERVICE})
        _, _, customer = self.http_client.post("/customers", body=attributes)
        return customer

    def update(self, id, *args, **kwargs):
        """
        Update a customer

        Updates a customer's information
        If the specified customer does not exist, this query will return an error
        **Notice** if you want to update a customer, you **must** make sure the customer's name is unique within the scope of the specified resource

        :calls: ``put /customers/{id}``
        :param int id: Unique identifier of a Customer.
        :param tuple *args: (optional) Single object representing Customer resource which attributes should be updated.
        :param dict **kwargs: (optional) Customer attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Customer resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Customer are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, customer = self.http_client.put("/customers/{id}".format(id=id), body=attributes)
        return customer

    def destroy(self, id):
        """
        Delete a customer

        Deletes an existing customer
        If the specified customer is assigned to any resource, we will remove this customer from all such resources
        If the specified customer does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /customers/{id}``
        :param int id: Unique identifier of a Customer.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/customers/{id}".format(id=id))
        return status_code == 204
