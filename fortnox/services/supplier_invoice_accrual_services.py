class SupplierInvoiceAccrualService(object):
    """
    :class:`fortnox.SupplierInvoiceAccrualService` is used by :class:`fortnox.Client` to make
    actions related to SupplierInvoiceAccrual resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for SupplierInvoiceAccrual to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['AccrualAccount', 'CostAccount', 'Description', 'SupplierInvoiceAccrualRows',
                            'StartDate', 'EndDate', 'SupplierInvoiceNumber', 'Period', 'Total']

    """
    SupplierInvoiceAccrualRows has the following structures,
        "SupplierInvoiceAccrualRows": [
              {
                "Account": 1790,
                "Credit": 6666.67,
                "Debit": 0
              },
              {
                "Account": 5820,
                "Credit": 0,
                "Debit": 6666.67
              },
              .................
        ]
    """

    SERVICE = "SupplierInvoiceAccrual"

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
        Retrieve all SupplierInvoiceAccrual

        Returns all SupplierInvoiceAccrual available to the Company, according to the parameters provided

        :calls: ``get /supplierinvoiceaccruals``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of SupplierInvoiceAccrual.
        :rtype: list
        """

        _, _, supplier_invoice_accruals = self.http_client.get("/supplierinvoiceaccruals", params=params)
        return supplier_invoice_accruals

    def retrieve(self, supplier_invoice_number):
        """
        Retrieve a single SupplierInvoiceAccrual

        Returns a single SupplierInvoiceAccrual according to the unique SupplierInvoiceAccrual ID provided
        If the specified SupplierInvoiceAccrual does not exist, this query returns an error

        :calls: ``get /supplierinvoiceaccruals/{supplier_invoice_number}``
        :param int id: Unique identifier of a SupplierInvoiceAccrual.
        :return: Dictionary that support attriubte-style access and represent SupplierInvoiceAccrual resource.
        :rtype: dict
        """
        _, _, supplier_invoice_accrual = self.http_client.get(
            "/supplierinvoiceaccruals/{supplier_invoice_number}".format(
                supplier_invoice_number=supplier_invoice_number))
        return supplier_invoice_accrual

    def create(self, *args, **kwargs):
        """
        Create a SupplierInvoiceAccrual

        Creates a new SupplierInvoiceAccrual
        **Notice** the SupplierInvoiceAccrual's name **must** be unique within the scope of the resource_type

        :calls: ``post /supplierinvoiceaccruals``
        :param tuple *args: (optional) Single object representing SupplierInvoiceAccrual resource.
        :param dict **kwargs: (optional) supplier_invoice_accrual attributes.
        :return: Dictionary that support attriubte-style access and represents newely created SupplierInvoiceAccrual resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for SupplierInvoiceAccrual are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, supplier_invoice_accrual = self.http_client.post("/supplierinvoiceaccruals", body=attributes)
        return supplier_invoice_accrual

    def update(self, supplier_invoice_number, *args, **kwargs):
        """
        Update a SupplierInvoiceAccrual

        Updates a SupplierInvoiceAccrual's information
        If the specified SupplierInvoiceAccrual does not exist, this query will return an error
        **Notice** if you want to update a SupplierInvoiceAccrual, you **must** make sure the SupplierInvoiceAccrual's name is unique within the scope of the specified resource

        :calls: ``put /supplierinvoiceaccruals/{supplier_invoice_number}``
        :param int id: Unique identifier of a SupplierInvoiceAccrual.
        :param tuple *args: (optional) Single object representing SupplierInvoiceAccrual resource which attributes should be updated.
        :param dict **kwargs: (optional) SupplierInvoiceAccrual attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated SupplierInvoiceAccrual resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for SupplierInvoiceAccrual are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, supplier_invoice_accrual = self.http_client.put(
            "/supplierinvoiceaccruals/{supplier_invoice_number}".format(
                supplier_invoice_number=supplier_invoice_number),
            body=attributes)
        return supplier_invoice_accrual

    def destroy(self, supplier_invoice_number):
        """
        Delete a SupplierInvoiceAccrual

        Deletes an existing SupplierInvoiceAccrual
        If the specified SupplierInvoiceAccrual is assigned to any resource, we will remove this SupplierInvoiceAccrual from all such resources
        If the specified SupplierInvoiceAccrual does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /supplierinvoiceaccruals/{supplier_invoice_number}``
        :param int id: Unique identifier of a SupplierInvoiceAccrual.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/supplierinvoiceaccruals/{supplier_invoice_number}".format(
            supplier_invoice_number=supplier_invoice_number))
        return status_code == 204
