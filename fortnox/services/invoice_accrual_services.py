class InvoiceAccrualService(object):
    """
    :class:`fortnox.InvoiceAccrualService` is used by :class:`fortnox.Client` to make
    actions related to InvoiceAccrual resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for InvoiceAccrual to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['AccrualAccount', 'StartDate', 'InvoiceAccrualRows', 'InvoiceNumber', 'Period',
                            'RevenueAccount', 'EndDate', 'Total']

    """
    InvoiceAccrualRows will have following structures:
        "InvoiceAccrualRows": [
          {
            "Account": 2990,
            "Credit": 0,
            "Debit": 2000
          },
          {
            "Account": 3990,
            "Credit": 2000,
            "Debit": 0
          },
          ...............
        ]
    """

    SERVICE = "InvoiceAccrual"

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
        Retrieve all InvoiceAccrual

        Returns all InvoiceAccrual available to the Company, according to the parameters provided

        :calls: ``get /invoiceaccruals``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of InvoiceAccrual.
        :rtype: list
        """

        _, _, invoice_accruals = self.http_client.get("/invoiceaccruals", params=params)
        return invoice_accruals

    def retrieve(self, invoice_number):
        """
        Retrieve a single InvoiceAccrual

        Returns a single InvoiceAccrual according to the unique InvoiceAccrual ID provided
        If the specified InvoiceAccrual does not exist, this query returns an error

        :calls: ``get /invoiceaccruals/{invoice_number}``
        :param int id: Unique identifier of a InvoiceAccrual.
        :return: Dictionary that support attriubte-style access and represent InvoiceAccrual resource.
        :rtype: dict
        """
        _, _, invoice_accrual = self.http_client.get(
            "/invoiceaccruals/{invoice_number}".format(invoice_number=invoice_number))
        return invoice_accrual

    def create(self, *args, **kwargs):
        """
        Create a InvoiceAccrual

        Creates a new InvoiceAccrual
        **Notice** the InvoiceAccrual's name **must** be unique within the scope of the resource_type

        :calls: ``post /invoiceaccruals``
        :param tuple *args: (optional) Single object representing InvoiceAccrual resource.
        :param dict **kwargs: (optional) invoice_accrual attributes.
        :return: Dictionary that support attriubte-style access and represents newely created InvoiceAccrual resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for InvoiceAccrual are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, invoice_accrual = self.http_client.post("/invoiceaccruals", body=attributes)
        return invoice_accrual

    def update(self, invoice_number, *args, **kwargs):
        """
        Update a InvoiceAccrual

        Updates a InvoiceAccrual's information
        If the specified InvoiceAccrual does not exist, this query will return an error
        **Notice** if you want to update a InvoiceAccrual, you **must** make sure the InvoiceAccrual's name is unique within the scope of the specified resource

        :calls: ``put /invoiceaccruals/{invoice_number}``
        :param int id: Unique identifier of a InvoiceAccrual.
        :param tuple *args: (optional) Single object representing InvoiceAccrual resource which attributes should be updated.
        :param dict **kwargs: (optional) InvoiceAccrual attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated InvoiceAccrual resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for InvoiceAccrual are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, invoice_accrual = self.http_client.put(
            "/invoiceaccruals/{invoice_number}".format(invoice_number=invoice_number), body=attributes)
        return invoice_accrual

    def destroy(self, invoice_number):
        """
        Delete a InvoiceAccrual

        Deletes an existing InvoiceAccrual
        If the specified InvoiceAccrual is assigned to any resource, we will remove this InvoiceAccrual from all such resources
        If the specified InvoiceAccrual does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /invoiceaccruals/{invoice_number}``
        :param int id: Unique identifier of a InvoiceAccrual.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete(
            "/invoiceaccruals/{invoice_number}".format(invoice_number=invoice_number))
        return status_code == 204
