class InvoiceService(object):
    """
    :class:`fortnox.InvoiceService` is used by :class:`fortnox.Client` to make
    actions related to InvoiceService resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Invoice to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['InvoiceRows', 'CustomerNumber']
    SERVICE = "Invoice"

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
        Retrieve all Invoices

        Returns all Invoices available to the Company, according to the parameters provided

        :calls: ``get /invoices``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Invoices.
        :rtype: list
        """

        _, _, invoices = self.http_client.get("/invoices", params=params)
        return invoices

    def retrieve(self, id):
        """
        Retrieve a single Invoice

        Returns a single Invoice according to the unique Invoice ID provided
        If the specified Invoice does not exist, this query returns an error

        :calls: ``get /invoices/{id}``
        :param int id: Unique identifier of an Invoice.
        :return: Dictionary that support attriubte-style access and represent Invoice resource.
        :rtype: dict
        """
        _, _, invoice = self.http_client.get("/invoices/{id}".format(id=id))
        return invoice

    def create(self, *args, **kwargs):
        """
        Create an Invoice

        Creates a new Invoice
        **Notice** the invoice's name **must** be unique within the scope of the resource_type

        :calls: ``post /invoices``
        :param tuple *args: (optional) Single object representing Invoice resource.
        :param dict **kwargs: (optional) Invoice attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Invoice resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Invoice are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, invoice = self.http_client.post("/invoices", body=attributes)
        return invoice

    def update(self, id, *args, **kwargs):
        """
        Update an Invoice

        Updates an invoice's information
        If the specified Invoice does not exist, this query will return an error
        **Notice** if you want to update an Invoice, you **must** make sure the Invoice's name is unique within the scope of the specified resource

        :calls: ``put /invoices/{id}``
        :param int id: Unique identifier of an Invoice.
        :param tuple *args: (optional) Single object representing Invoice resource which attributes should be updated.
        :param dict **kwargs: (optional) Invoice attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Invoice resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Invoice are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, invoice = self.http_client.put("/invoices/{id}".format(id=id), body=attributes)
        return invoice
