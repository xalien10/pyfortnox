class SupplierInvoiceService(object):
    """
    :class:`fortnox.SupplierInvoiceService` is used by :class:`fortnox.Client` to make
    actions related to SupplierInvoice resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for SupplierInvoice to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Currency', 'CurrencyRate', 'CurrencyUnit', 'InvoiceDate', 'SupplierInvoiceRows',
                            'DueDate', 'SupplierNumber', 'Total', 'VAT', 'VATType', 'SalesType']

    """
    SupplierInvoiceRows has the following structures:
        "SupplierInvoiceRows": [
              {
                "Account": 2440,
                "Code": "TOT",
                "AccountDescription": "Leverantörsskulder",
                "Debit": 0,
                "Credit": 10000,
                "Total": -10000
              },
              {
                "Account": 2641,
                "Code": "VAT",
                "AccountDescription": "Debiterad ingående moms",
                "Debit": 2000,
                "Credit": 0,
                "Total": 2000
              },
              {
                "Account": 6210,
                "Code": "PRE",
                "AccountDescription": "Telekommunikation",
                "Debit": 8000,
                "Credit": 0,
                "Total": 8000
              },
              ..................
        ]
    """

    SERVICE = "SupplierInvoice"

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
        Retrieve all SupplierInvoice

        Returns all SupplierInvoice available to the Company, according to the parameters provided

        :calls: ``get /supplierinvoices``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of SupplierInvoice.
        :rtype: list
        """

        _, _, supplier_invoices = self.http_client.get("/supplierinvoices", params=params)
        return supplier_invoices

    def retrieve(self, given_number):
        """
        Retrieve a single SupplierInvoice

        Returns a single SupplierInvoice according to the unique SupplierInvoice ID provided
        If the specified SupplierInvoice does not exist, this query returns an error

        :calls: ``get /supplierinvoices/{given_number}``
        :param int id: Unique identifier of a SupplierInvoice.
        :return: Dictionary that support attriubte-style access and represent SupplierInvoice resource.
        :rtype: dict
        """
        _, _, supplier_invoice = self.http_client.get(
            "/supplierinvoices/{given_number}".format(given_number=given_number))
        return supplier_invoice

    def create(self, *args, **kwargs):
        """
        Create a SupplierInvoice

        Creates a new SupplierInvoice
        **Notice** the SupplierInvoice's name **must** be unique within the scope of the resource_type

        :calls: ``post /supplierinvoices``
        :param tuple *args: (optional) Single object representing SupplierInvoice resource.
        :param dict **kwargs: (optional) supplier_invoice attributes.
        :return: Dictionary that support attriubte-style access and represents newely created SupplierInvoice resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for SupplierInvoice are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, supplier_invoice = self.http_client.post("/supplierinvoices", body=attributes)
        return supplier_invoice

    def update(self, given_number, *args, **kwargs):
        """
        Update a SupplierInvoice

        Updates a SupplierInvoice's information
        If the specified SupplierInvoice does not exist, this query will return an error
        **Notice** if you want to update a SupplierInvoice, you **must** make sure the SupplierInvoice's name is unique within the scope of the specified resource

        :calls: ``put /supplierinvoices/{given_number}``
        :param int id: Unique identifier of a SupplierInvoice.
        :param tuple *args: (optional) Single object representing SupplierInvoice resource which attributes should be updated.
        :param dict **kwargs: (optional) SupplierInvoice attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated SupplierInvoice resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for SupplierInvoice are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, supplier_invoice = self.http_client.put(
            "/supplierinvoices/{given_number}".format(given_number=given_number), body=attributes)
        return supplier_invoice
