class NoxFinansInvoiceService(object):
    """
    :class:`fortnox.NoxFinansInvoiceService` is used by :class:`fortnox.Client` to make
    actions related to NoxFinansInvoice resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for NoxFinansInvoice to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['InvoiceNumber', 'SendMethod', 'Service']
    SERVICE = "NoxFinansInvoice"

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
        Retrieve all NoxFinansInvoice

        Returns all NoxFinansInvoice available to the Company, according to the parameters provided

        :calls: ``get /noxfinansinvoices``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of NoxFinansInvoice.
        :rtype: list
        """

        _, _, nox_finans_invoices = self.http_client.get("/noxfinansinvoices", params=params)
        return nox_finans_invoices

    def retrieve(self, invoice_number):
        """
        Retrieve a single NoxFinansInvoice

        Returns a single NoxFinansInvoice according to the unique NoxFinansInvoice ID provided
        If the specified NoxFinansInvoice does not exist, this query returns an error

        :calls: ``get /noxfinansinvoices/{invoice_number}``
        :param int id: Unique identifier of a NoxFinansInvoice.
        :return: Dictionary that support attriubte-style access and represent NoxFinansInvoice resource.
        :rtype: dict
        """
        _, _, nox_finans_invoice = self.http_client.get(
            "/noxfinansinvoices/{invoice_number}".format(invoice_number=invoice_number))
        return nox_finans_invoice

    def create(self, *args, **kwargs):
        """
        Create a NoxFinansInvoice

        Creates a new NoxFinansInvoice
        **Notice** the NoxFinansInvoice's name **must** be unique within the scope of the resource_type

        :calls: ``post /noxfinansinvoices``
        :param tuple *args: (optional) Single object representing NoxFinansInvoice resource.
        :param dict **kwargs: (optional) nox_finans_invoice attributes.
        :return: Dictionary that support attriubte-style access and represents newely created NoxFinansInvoice resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for NoxFinansInvoice are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, nox_finans_invoice = self.http_client.post("/noxfinansinvoices", body=attributes)
        return nox_finans_invoice

    def update(self, invoice_number, *args, **kwargs):
        """
        Update a NoxFinansInvoice

        Updates a NoxFinansInvoice's information
        If the specified NoxFinansInvoice does not exist, this query will return an error
        **Notice** if you want to update a NoxFinansInvoice, you **must** make sure the NoxFinansInvoice's name is unique within the scope of the specified resource

        :calls: ``put /noxfinansinvoices/{invoice_number}``
        :param int id: Unique identifier of a NoxFinansInvoice.
        :param tuple *args: (optional) Single object representing NoxFinansInvoice resource which attributes should be updated.
        :param dict **kwargs: (optional) NoxFinansInvoice attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated NoxFinansInvoice resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for NoxFinansInvoice are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, nox_finans_invoice = self.http_client.put(
            "/noxfinansinvoices/{invoice_number}".format(invoice_number=invoice_number), body=attributes)
        return nox_finans_invoice

    def destroy(self, invoice_number):
        """
        Delete a NoxFinansInvoice

        Deletes an existing NoxFinansInvoice
        If the specified NoxFinansInvoice is assigned to any resource, we will remove this NoxFinansInvoice from all such resources
        If the specified NoxFinansInvoice does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /noxfinansinvoices/{invoice_number}``
        :param int id: Unique identifier of a NoxFinansInvoice.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete(
            "/noxfinansinvoices/{invoice_number}".format(invoice_number=invoice_number))
        return status_code == 204
