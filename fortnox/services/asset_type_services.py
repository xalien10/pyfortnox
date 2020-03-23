class AssetTypeService(object):
    """
    :class:`fortnox.AssetTypeService` is used by :class:`fortnox.Client` to make
    actions related to Asset Type resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for AssetType to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Number', 'Description', 'AccountAssetId',
                            'AccountDepreciationId', 'AccountValueLossId',
                            'Type']
    SERVICE = "AssetType"

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
        Retrieve all AssetTypes

        Returns all AssetTypes available to the Company, according to the parameters provided

        :calls: ``get /assets/types``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of AssetTypes.
        :rtype: list
        """

        _, _, asset_types = self.http_client.get("/assets/types", params=params)
        return asset_types[1:]

    def retrieve(self, id):
        """
        Retrieve a single AssetType

        Returns a single AssetType according to the unique AssetType ID provided
        If the specified AssetType does not exist, this query returns an error

        :calls: ``get /assets/types/{id}``
        :param int id: Unique identifier of an AssetType.
        :return: Dictionary that support attriubte-style access and represent AssetType resource.
        :rtype: dict
        """
        _, _, asset_type = self.http_client.get("/assets/types/{id}".format(id=id))
        return asset_type

    def create(self, *args, **kwargs):
        """
        Create an AssetType

        Creates a new AssetType
        **Notice** the AssetType's name **must** be unique within the scope of the resource_type

        :calls: ``post /assets/types``
        :param tuple *args: (optional) Single object representing AssetType resource.
        :param dict **kwargs: (optional) AssetType attributes.
        :return: Dictionary that support attriubte-style access and represents newely created AssetType resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for AssetType are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items() if k in self.OPTS_KEYS_TO_PERSIST)
        attributes.update({'service': self.SERVICE})
        _, _, asset_type = self.http_client.post("/assets/types", body=attributes)
        return asset_type

    def update(self, id, *args, **kwargs):
        """
        Update an AssetType

        Updates an AssetType's information
        If the specified AssetType does not exist, this query will return an error
        **Notice** if you want to update an AssetType, you **must** make sure the AssetType's name is unique within the scope of the specified resource

        :calls: ``put /assets/types/{id}``
        :param int id: Unique identifier of an AssetType.
        :param tuple *args: (optional) Single object representing AssetType resource which attributes should be updated.
        :param dict **kwargs: (optional) AssetType attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated AssetType resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for AssetType are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, asset_type = self.http_client.put("/assets/types/{id}".format(id=id), body=attributes)
        return asset_type

    def destroy(self, id):
        """
        Delete an AssetType

        Deletes an existing AssetType
        If the specified AssetType is assigned to any resource, we will remove this AssetType from all such resources
        If the specified AssetType does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /assets/types/{id}``
        :param int id: Unique identifier of an AssetType.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/assets/types/{id}".format(id=id))
        return status_code == 200
