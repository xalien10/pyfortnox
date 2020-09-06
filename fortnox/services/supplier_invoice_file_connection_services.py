class SupplierInvoiceFileConnectionService(object):
    """
    :class:`fortnox.SupplierInvoiceFileConnectionService` is used by :class:`fortnox.Client` to make
    actions related to SupplierInvoiceFileConnection resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for SupplierInvoiceFileConnection to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['FileId', 'SupplierInvoiceNumber']
    SERVICE = "SupplierInvoiceFileConnection"

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
        Retrieve all SupplierInvoiceFileConnection

        Returns all SupplierInvoiceFileConnection available to the Company, according to the parameters provided

        :calls: ``get /supplierinvoicefileconnections``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of SupplierInvoiceFileConnection.
        :rtype: list
        """

        _, _, supplier_invoice_file_connections = self.http_client.get("/supplierinvoicefileconnections", params=params)
        return supplier_invoice_file_connections

    def retrieve(self, file_id):
        """
        Retrieve a single SupplierInvoiceFileConnection

        Returns a single SupplierInvoiceFileConnection according to the unique SupplierInvoiceFileConnection ID provided
        If the specified SupplierInvoiceFileConnection does not exist, this query returns an error

        :calls: ``get /supplierinvoicefileconnections/{file_id}``
        :param int id: Unique identifier of a SupplierInvoiceFileConnection.
        :return: Dictionary that support attriubte-style access and represent SupplierInvoiceFileConnection resource.
        :rtype: dict
        """
        _, _, supplier_invoice_file_connection = self.http_client.get(
            "/supplierinvoicefileconnections/{file_id}".format(file_id=file_id))
        return supplier_invoice_file_connection

    def create(self, *args, **kwargs):
        """
        Create a SupplierInvoiceFileConnection

        Creates a new SupplierInvoiceFileConnection
        **Notice** the SupplierInvoiceFileConnection's name **must** be unique within the scope of the resource_type

        :calls: ``post /supplierinvoicefileconnections``
        :param tuple *args: (optional) Single object representing SupplierInvoiceFileConnection resource.
        :param dict **kwargs: (optional) supplier_invoice_file_connection attributes.
        :return: Dictionary that support attriubte-style access and represents newely created SupplierInvoiceFileConnection resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for SupplierInvoiceFileConnection are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, supplier_invoice_file_connection = self.http_client.post("/supplierinvoicefileconnections",
                                                                       body=attributes)
        return supplier_invoice_file_connection

    def destroy(self, file_id):
        """
        Delete a SupplierInvoiceFileConnection

        Deletes an existing SupplierInvoiceFileConnection
        If the specified SupplierInvoiceFileConnection is assigned to any resource, we will remove this SupplierInvoiceFileConnection from all such resources
        If the specified SupplierInvoiceFileConnection does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /supplierinvoicefileconnections/{file_id}``
        :param int id: Unique identifier of a SupplierInvoiceFileConnection.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/supplierinvoicefileconnections/{file_id}".format(file_id=file_id))
        return status_code == 204
