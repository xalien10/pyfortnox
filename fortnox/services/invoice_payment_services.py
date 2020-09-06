class InvoicePaymentService(object):
    """
    :class:`fortnox.InvoicePaymentService` is used by :class:`fortnox.Client` to make
    actions related to InvoicePayment resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for InvoicePayment to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['InvoiceNumber', 'Amount', 'AmountCurrency']
    SERVICE = "InvoicePayment"

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
        Retrieve all InvoicePayment

        Returns all InvoicePayment available to the Company, according to the parameters provided

        :calls: ``get /invoicepayments``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of InvoicePayment.
        :rtype: list
        """

        _, _, invoice_payments = self.http_client.get("/invoicepayments", params=params)
        return invoice_payments

    def retrieve(self, number):
        """
        Retrieve a single InvoicePayment

        Returns a single InvoicePayment according to the unique InvoicePayment ID provided
        If the specified InvoicePayment does not exist, this query returns an error

        :calls: ``get /invoicepayments/{number}``
        :param int id: Unique identifier of a InvoicePayment.
        :return: Dictionary that support attriubte-style access and represent InvoicePayment resource.
        :rtype: dict
        """
        _, _, invoice_payment = self.http_client.get("/invoicepayments/{number}".format(number=number))
        return invoice_payment

    def create(self, *args, **kwargs):
        """
        Create a InvoicePayment

        Creates a new InvoicePayment
        **Notice** the InvoicePayment's name **must** be unique within the scope of the resource_type

        :calls: ``post /invoicepayments``
        :param tuple *args: (optional) Single object representing InvoicePayment resource.
        :param dict **kwargs: (optional) invoice_payment attributes.
        :return: Dictionary that support attriubte-style access and represents newely created InvoicePayment resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for InvoicePayment are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, invoice_payment = self.http_client.post("/invoicepayments", body=attributes)
        return invoice_payment

    def update(self, number, *args, **kwargs):
        """
        Update a InvoicePayment

        Updates a InvoicePayment's information
        If the specified InvoicePayment does not exist, this query will return an error
        **Notice** if you want to update a InvoicePayment, you **must** make sure the InvoicePayment's name is unique within the scope of the specified resource

        :calls: ``put /invoicepayments/{number}``
        :param int id: Unique identifier of a InvoicePayment.
        :param tuple *args: (optional) Single object representing InvoicePayment resource which attributes should be updated.
        :param dict **kwargs: (optional) InvoicePayment attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated InvoicePayment resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for InvoicePayment are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, invoice_payment = self.http_client.put("/invoicepayments/{number}".format(number=number), body=attributes)
        return invoice_payment

    def destroy(self, number):
        """
        Delete a InvoicePayment

        Deletes an existing InvoicePayment
        If the specified InvoicePayment is assigned to any resource, we will remove this InvoicePayment from all such resources
        If the specified InvoicePayment does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /invoicepayments/{number}``
        :param int id: Unique identifier of a InvoicePayment.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/invoicepayments/{number}".format(number=number))
        return status_code == 204
