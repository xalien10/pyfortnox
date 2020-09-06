class SupplierInvoiceExternalURLConnectionService(object):
    """
    :class:`fortnox.SupplierInvoiceExternalURLConnectionService` is used by :class:`fortnox.Client` to make
    actions related to SupplierInvoiceExternalURLConnection resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for SupplierInvoiceExternalURLConnection to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['SupplierInvoiceNumber', 'SupplierInvoiceNumber']
    SERVICE = "SupplierInvoiceExternalURLConnection"

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
        Retrieve all SupplierInvoiceExternalURLConnection

        Returns all SupplierInvoiceExternalURLConnection available to the Company, according to the parameters provided

        :calls: ``get /supplierinvoiceexternalurlconnections``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of SupplierInvoiceExternalURLConnection.
        :rtype: list
        """

        _, _, supplier_invoice_external_url_connections = self.http_client.get("/supplierinvoiceexternalurlconnections",
                                                                               params=params)
        return supplier_invoice_external_url_connections

    def retrieve(self, id):
        """
        Retrieve a single SupplierInvoiceExternalURLConnection

        Returns a single SupplierInvoiceExternalURLConnection according to the unique SupplierInvoiceExternalURLConnection ID provided
        If the specified SupplierInvoiceExternalURLConnection does not exist, this query returns an error

        :calls: ``get /supplierinvoiceexternalurlconnections/{id}``
        :param int id: Unique identifier of a SupplierInvoiceExternalURLConnection.
        :return: Dictionary that support attriubte-style access and represent SupplierInvoiceExternalURLConnection resource.
        :rtype: dict
        """
        _, _, supplier_invoice_external_url_connection = self.http_client.get(
            "/supplierinvoiceexternalurlconnections/{id}".format(id=id))
        return supplier_invoice_external_url_connection

    def create(self, *args, **kwargs):
        """
        Create a SupplierInvoiceExternalURLConnection

        Creates a new SupplierInvoiceExternalURLConnection
        **Notice** the SupplierInvoiceExternalURLConnection's name **must** be unique within the scope of the resource_type

        :calls: ``post /supplierinvoiceexternalurlconnections``
        :param tuple *args: (optional) Single object representing SupplierInvoiceExternalURLConnection resource.
        :param dict **kwargs: (optional) supplier_invoice_external_url_connection attributes.
        :return: Dictionary that support attriubte-style access and represents newely created SupplierInvoiceExternalURLConnection resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for SupplierInvoiceExternalURLConnection are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, supplier_invoice_external_url_connection = self.http_client.post("/supplierinvoiceexternalurlconnections",
                                                                               body=attributes)
        return supplier_invoice_external_url_connection

    def update(self, id, *args, **kwargs):
        """
        Update a SupplierInvoiceExternalURLConnection

        Updates a SupplierInvoiceExternalURLConnection's information
        If the specified SupplierInvoiceExternalURLConnection does not exist, this query will return an error
        **Notice** if you want to update a SupplierInvoiceExternalURLConnection, you **must** make sure the SupplierInvoiceExternalURLConnection's name is unique within the scope of the specified resource

        :calls: ``put /supplierinvoiceexternalurlconnections/{id}``
        :param int id: Unique identifier of a SupplierInvoiceExternalURLConnection.
        :param tuple *args: (optional) Single object representing SupplierInvoiceExternalURLConnection resource which attributes should be updated.
        :param dict **kwargs: (optional) SupplierInvoiceExternalURLConnection attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated SupplierInvoiceExternalURLConnection resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for SupplierInvoiceExternalURLConnection are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, supplier_invoice_external_url_connection = self.http_client.put(
            "/supplierinvoiceexternalurlconnections/{id}".format(id=id), body=attributes)
        return supplier_invoice_external_url_connection

    def destroy(self, id):
        """
        Delete a SupplierInvoiceExternalURLConnection

        Deletes an existing SupplierInvoiceExternalURLConnection
        If the specified SupplierInvoiceExternalURLConnection is assigned to any resource, we will remove this SupplierInvoiceExternalURLConnection from all such resources
        If the specified SupplierInvoiceExternalURLConnection does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /supplierinvoiceexternalurlconnections/{id}``
        :param int id: Unique identifier of a SupplierInvoiceExternalURLConnection.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/supplierinvoiceexternalurlconnections/{id}".format(id=id))
        return status_code == 204
