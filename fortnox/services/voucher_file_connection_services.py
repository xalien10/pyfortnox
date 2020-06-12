class VoucherFileConnectionService(object):
    """
    :class:`fortnox.VoucherFileConnectionService` is used by :class:`fortnox.Client` to make
    actions related to VoucherFileConnection resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for VoucherFileConnection to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['FileId', 'VoucherNumber', 'VoucherSeries']
    SERVICE = "VoucherFileConnection"

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
        Retrieve all VoucherFileConnection

        Returns all VoucherFileConnection available to the Company, according to the parameters provided

        :calls: ``get /voucherfileconnections``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of VoucherFileConnection.
        :rtype: list
        """

        _, _, voucher_file_connections = self.http_client.get("/voucherfileconnections", params=params)
        return voucher_file_connections

    def retrieve(self, file_id):
        """
        Retrieve a single VoucherFileConnection

        Returns a single VoucherFileConnection according to the unique VoucherFileConnection ID provided
        If the specified VoucherFileConnection does not exist, this query returns an error

        :calls: ``get /voucherfileconnections/{file_id}``
        :param int id: Unique identifier of a VoucherFileConnection.
        :return: Dictionary that support attriubte-style access and represent VoucherFileConnection resource.
        :rtype: dict
        """
        _, _, voucher_file_connection = self.http_client.get(
            "/voucherfileconnections/{file_id}".format(file_id=file_id))
        return voucher_file_connection

    def create(self, *args, **kwargs):
        """
        Create a VoucherFileConnection

        Creates a new VoucherFileConnection
        **Notice** the VoucherFileConnection's name **must** be unique within the scope of the resource_type

        :calls: ``post /voucherfileconnections`` or ``/voucherfileconnections?financialyeardate={financialyeardate}``
        :param tuple *args: (optional) Single object representing VoucherFileConnection resource.
        :param dict **kwargs: (optional) voucher_file_connection attributes.
        :return: Dictionary that support attriubte-style access and represents newely created VoucherFileConnection resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for VoucherFileConnection are missing')

        attributes = args[0] if args else kwargs

        financialyeardate = attributes.get('financialyeardate', None)
        if financialyeardate:
            path_name = "/voucherfileconnections?financialyeardate={financialyeardate}".format(
                financialyeardate=financialyeardate)
        else:
            path_name = "/voucherfileconnections"

        attributes = dict((k, v) for k, v in attributes.items() if k in self.OPTS_KEYS_TO_PERSIST)
        attributes.update({'service': self.SERVICE})
        _, _, voucher_file_connection = self.http_client.post(path_name, body=attributes)
        return voucher_file_connection

    def destroy(self, file_id):
        """
        Delete a VoucherFileConnection

        Deletes an existing VoucherFileConnection
        If the specified VoucherFileConnection is assigned to any resource, we will remove this VoucherFileConnection from all such resources
        If the specified VoucherFileConnection does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /voucherfileconnections/{file_id}``
        :param int id: Unique identifier of a VoucherFileConnection.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/voucherfileconnections/{file_id}".format(file_id=file_id))
        return status_code == 204
