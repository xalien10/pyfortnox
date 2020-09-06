class AssetService(object):
    """
    :class:`fortnox.AssetService` is used by :class:`fortnox.Client` to make
    actions related to Assets resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Asset to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Number', 'Description', 'TypeId', 'AcquisitionDate',
                            'AcquisitionStart', 'DepreciationFinal', 'AcquisitionValue']
    SERVICE = "Asset"

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
        Retrieve all Assets

        Returns all Assets available to the Company, according to the parameters provided

        :calls: ``get /assets``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Assets.
        :rtype: list
        """

        _, _, assets = self.http_client.get("/assets", params=params)
        return assets

    def depreciation_list(self, to_date, **params):
        """
        Retrieve all deprecated assets

        Returns all deprecated assets available to the Company, according to the parameters provided

        :calls: ``get /assets/depreciations/{to_date}``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of deprecated assets.
        :rtype: list
        """

        _, _, deprecated_assets = self.http_client.get("/assets/depreciations/{to_date}".format(to_date=to_date),
                                                       params=params)
        return deprecated_assets[1:]

    def retrieve(self, id):
        """
        Retrieve a single Asset

        Returns a single Assets according to the unique Assets ID provided
        If the specified Asset does not exist, this query returns an error

        :calls: ``get /assets/{id}``
        :param int id: Unique identifier of an Asset.
        :return: Dictionary that support attriubte-style access and represent Asset resource.
        :rtype: dict
        """
        _, _, asset = self.http_client.get("/assets/{id}".format(id=id))
        return asset

    def create(self, *args, **kwargs):
        """
        Create an Asset

        Creates an new Asset
        **Notice** the Asset's name **must** be unique within the scope of the resource_type

        :calls: ``post /assets``
        :param tuple *args: (optional) Single object representing Asset resource.
        :param dict **kwargs: (optional) Asset attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Asset resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Asset are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, asset = self.http_client.post("/assets", body=attributes)
        return asset

    def update(self, id, *args, **kwargs):
        """
        Update an Asset

        Updates an Asset's information
        If the specified Asset does not exist, this query will return an error
        **Notice** if you want to update an Asset, you **must** make sure the Asset's name is unique within the scope of the specified resource

        :calls: ``put /assets/{id}``
        :param int id: Unique identifier of an Asset.
        :param tuple *args: (optional) Single object representing Asset resource which attributes should be updated.
        :param dict **kwargs: (optional) Asset attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Asset resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Asset are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, asset = self.http_client.put("/assets/{id}".format(id=id), body=attributes)
        return asset

    def destroy(self, id):
        """
        Delete an Asset

        Deletes an existing Asset
        If the specified Asset is assigned to any resource, we will remove this Asset from all such resources
        If the specified Asset does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /assets/{id}``
        :param int id: Unique identifier of an Asset.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/assets/{id}".format(id=id))
        return status_code == 200

    def depreciate(self, *args, **kwargs):
        """
        Depreciate Assets

        Updates an Asset's information
        If the specified Asset does not exist, this query will return an error
        **Notice** if you want to update an Asset, you **must** make sure the Asset's name is unique within the scope of the specified resource

        :calls: ``put /assets/depreciate``
        :param int id: Unique identifier of an Asset.
        :param tuple *args: (optional) Single object representing Asset resource which attributes should be updated.
        :param dict **kwargs: (optional) Asset attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Asset resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Asset are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, asset = self.http_client.post("/assets/depreciate", body=attributes)
        return asset

    def write_up(self, id, *args, **kwargs):
        """
        Update an Asset

        Asset's Write Up information
        If the specified Asset does not exist, this query will return an error
        **Notice** if you want to update an Asset, you **must** make sure the Asset's name is unique within the scope of the specified resource

        :calls: ``put /assets/writeup/{id}``
        :param int id: Unique identifier of an Asset.
        :param tuple *args: (optional) Single object representing Asset resource which attributes should be updated.
        :param dict **kwargs: (optional) Asset attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Asset resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Asset Write Up are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, asset = self.http_client.put("/assets/writeup/{id}".format(id=id), body=attributes)
        return asset

    def write_down(self, id, *args, **kwargs):
        """
        Write Down an Asset

        Updates an Asset's information
        If the specified Asset does not exist, this query will return an error
        **Notice** if you want to update an Asset, you **must** make sure the Asset's name is unique within the scope of the specified resource

        :calls: ``put /assets/writedown/{id}``
        :param int id: Unique identifier of an Asset.
        :param tuple *args: (optional) Single object representing Asset resource which attributes should be updated.
        :param dict **kwargs: (optional) Asset attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Asset resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Asset Write Down are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, asset = self.http_client.put("/assets/writedown/{id}".format(id=id), body=attributes)
        return asset

    def scrap(self, id, *args, **kwargs):
        """
        Scrap Down an Asset

        Updates an Asset's information
        If the specified Asset does not exist, this query will return an error
        **Notice** if you want to update an Asset, you **must** make sure the Asset's name is unique within the scope of the specified resource

        :calls: ``put /assets/scrap/{id}``
        :param int id: Unique identifier of an Asset.
        :param tuple *args: (optional) Single object representing Asset resource which attributes should be updated.
        :param dict **kwargs: (optional) Asset attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Asset resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Asset Scrap are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, asset = self.http_client.put("/assets/scrap/{id}".format(id=id), body=attributes)
        return asset

    def sell(self, id, *args, **kwargs):
        """
        Sell an Asset

        An Asset's sell information
        If the specified Asset does not exist, this query will return an error
        **Notice** if you want to update an Asset, you **must** make sure the Asset's name is unique within the scope of the specified resource

        :calls: ``put /assets/sell/{id}``
        :param int id: Unique identifier of an Asset.
        :param tuple *args: (optional) Single object representing Asset resource which attributes should be updated.
        :param dict **kwargs: (optional) Asset attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Asset resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Asset are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, asset = self.http_client.put("/assets/sell/{id}".format(id=id), body=attributes)
        return asset
