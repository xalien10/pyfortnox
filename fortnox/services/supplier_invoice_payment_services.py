class SupplierInvoicePaymentService(object):
    """
    :class:`fortnox.SupplierInvoicePaymentService` is used by :class:`fortnox.Client` to make
    actions related to SupplierInvoicePayment resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for SupplierInvoicePayment to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Amount', 'InvoiceNumber']
    SERVICE = "SupplierInvoicePayment"

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
        Retrieve all SupplierInvoicePayment

        Returns all SupplierInvoicePayment available to the Company, according to the parameters provided

        :calls: ``get /supplierinvoicepayments``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of SupplierInvoicePayment.
        :rtype: list
        """

        _, _, supplier_invoice_payments = self.http_client.get("/supplierinvoicepayments", params=params)
        return supplier_invoice_payments

    def retrieve(self, number):
        """
        Retrieve a single SupplierInvoicePayment

        Returns a single SupplierInvoicePayment according to the unique SupplierInvoicePayment ID provided
        If the specified SupplierInvoicePayment does not exist, this query returns an error

        :calls: ``get /supplierinvoicepayments/{number}``
        :param int id: Unique identifier of a SupplierInvoicePayment.
        :return: Dictionary that support attriubte-style access and represent SupplierInvoicePayment resource.
        :rtype: dict
        """
        _, _, supplier_invoice_payment = self.http_client.get("/supplierinvoicepayments/{number}".format(number=number))
        return supplier_invoice_payment

    def create(self, *args, **kwargs):
        """
        Create a SupplierInvoicePayment

        Creates a new SupplierInvoicePayment
        **Notice** the SupplierInvoicePayment's name **must** be unique within the scope of the resource_type

        :calls: ``post /supplierinvoicepayments``
        :param tuple *args: (optional) Single object representing SupplierInvoicePayment resource.
        :param dict **kwargs: (optional) supplier_invoice_payment attributes.
        :return: Dictionary that support attriubte-style access and represents newely created SupplierInvoicePayment resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for SupplierInvoicePayment are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, supplier_invoice_payment = self.http_client.post("/supplierinvoicepayments", body=attributes)
        return supplier_invoice_payment

    def update(self, number, *args, **kwargs):
        """
        Update a SupplierInvoicePayment

        Updates a SupplierInvoicePayment's information
        If the specified SupplierInvoicePayment does not exist, this query will return an error
        **Notice** if you want to update a SupplierInvoicePayment, you **must** make sure the SupplierInvoicePayment's name is unique within the scope of the specified resource

        :calls: ``put /supplierinvoicepayments/{number}``
        :param int id: Unique identifier of a SupplierInvoicePayment.
        :param tuple *args: (optional) Single object representing SupplierInvoicePayment resource which attributes should be updated.
        :param dict **kwargs: (optional) SupplierInvoicePayment attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated SupplierInvoicePayment resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for SupplierInvoicePayment are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, supplier_invoice_payment = self.http_client.put("/supplierinvoicepayments/{number}".format(number=number),
                                                              body=attributes)
        return supplier_invoice_payment

    def destroy(self, number):
        """
        Delete a SupplierInvoicePayment

        Deletes an existing SupplierInvoicePayment
        If the specified SupplierInvoicePayment is assigned to any resource, we will remove this SupplierInvoicePayment from all such resources
        If the specified SupplierInvoicePayment does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /supplierinvoicepayments/{number}``
        :param int id: Unique identifier of a SupplierInvoicePayment.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/supplierinvoicepayments/{number}".format(number=number))
        return status_code == 204
