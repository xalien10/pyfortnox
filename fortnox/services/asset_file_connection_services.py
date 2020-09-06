class AssetFileConnectionService(object):
    """
    :class:`fortnox.AssetFileConnectionService File Connection` is used by :class:`fortnox.Client` to make
    actions related to Asset File Connection resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Asset File Connection to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['FileId', 'AssetId']
    SERVICE = "AssetFileConnection"

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
        Retrieve all Asset File Connection

        Returns all Asset File Connection available to the Company, according to the parameters provided

        :calls: ``get /assetfileconnections``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Customers.
        :rtype: list
        """

        _, _, asset_file_connections = self.http_client.get("/assetfileconnections", params=params)
        return asset_file_connections

    def retrieve(self, file_id):
        """
        Retrieve a single Asset File Connection

        Returns a single Asset File Connection according to the unique Asset File Connection ID provided
        If the specified Asset File Connection does not exist, this query returns an error

        :calls: ``get /assetfileconnections/{file_id}``
        :param int id: Unique identifier of a Asset File Connection.
        :return: Dictionary that support attriubte-style access and represent Asset File Connection resource.
        :rtype: dict
        """
        _, _, asset_file_connection = self.http_client.get("/assetfileconnections/{file_id}".format(file_id=file_id))
        return asset_file_connection

    def create(self, *args, **kwargs):
        """
        Create a Asset File Connection

        Creates a new Asset File Connection
        **Notice** the asset file connection's name **must** be unique within the scope of the resource_type

        :calls: ``post /assetfileconnections``
        :param tuple *args: (optional) Single object representing Asset File Connection resource.
        :param dict **kwargs: (optional) Customer attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Asset File Connection resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Asset File Connection are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, asset_file_connection = self.http_client.post("/assetfileconnections", body=attributes)
        return asset_file_connection

    def destroy(self, file_id):
        """
        Delete a Asset File Connection

        Deletes an existing Asset File Connection
        If the specified Asset File Connection is assigned to any resource, we will remove this Asset File Connection from all such resources
        If the specified Asset File Connection does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /assetfileconnections/{file_id}``
        :param int id: Unique identifier of a Asset File Connection.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/assetfileconnections/{file_id}".format(file_id=file_id))
        return status_code == 204
