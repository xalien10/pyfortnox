class UnitService(object):
    """
    :class:`fortnox.UnitService` is used by :class:`fortnox.Client` to make
    actions related to Unit resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Unit to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Code', 'Description']
    SERVICE = "Unit"

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
        Retrieve all Unit

        Returns all Unit available to the Company, according to the parameters provided

        :calls: ``get /units``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Unit.
        :rtype: list
        """

        _, _, units = self.http_client.get("/units", params=params)
        return units

    def retrieve(self, code):
        """
        Retrieve a single Unit

        Returns a single Unit according to the unique Unit ID provided
        If the specified Unit does not exist, this query returns an error

        :calls: ``get /units/{code}``
        :param int id: Unique identifier of a Unit.
        :return: Dictionary that support attriubte-style access and represent Unit resource.
        :rtype: dict
        """
        _, _, unit = self.http_client.get("/units/{code}".format(code=code))
        return unit

    def create(self, *args, **kwargs):
        """
        Create a Unit

        Creates a new Unit
        **Notice** the Unit's name **must** be unique within the scope of the resource_type

        :calls: ``post /units``
        :param tuple *args: (optional) Single object representing Unit resource.
        :param dict **kwargs: (optional) unit attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Unit resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Unit are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, unit = self.http_client.post("/units", body=attributes)
        return unit

    def update(self, code, *args, **kwargs):
        """
        Update a Unit

        Updates a Unit's information
        If the specified Unit does not exist, this query will return an error
        **Notice** if you want to update a Unit, you **must** make sure the Unit's name is unique within the scope of the specified resource

        :calls: ``put /units/{code}``
        :param int id: Unique identifier of a Unit.
        :param tuple *args: (optional) Single object representing Unit resource which attributes should be updated.
        :param dict **kwargs: (optional) Unit attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Unit resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Unit are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, unit = self.http_client.put("/units/{code}".format(code=code), body=attributes)
        return unit

    def destroy(self, code):
        """
        Delete a Unit

        Deletes an existing Unit
        If the specified Unit is assigned to any resource, we will remove this Unit from all such resources
        If the specified Unit does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /units/{code}``
        :param int id: Unique identifier of a Unit.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/units/{code}".format(code=code))
        return status_code == 204
