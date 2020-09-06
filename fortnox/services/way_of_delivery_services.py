class WayOfDeliveryService(object):
    """
    :class:`fortnox.WayOfDeliveryService` is used by :class:`fortnox.Client` to make
    actions related to WayOfDelivery resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for WayOfDelivery to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Code', 'Description']
    SERVICE = "WayOfDelivery"

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
        Retrieve all WayOfDelivery

        Returns all WayOfDelivery available to the Company, according to the parameters provided

        :calls: ``get /wayofdeliveries``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of WayOfDelivery.
        :rtype: list
        """

        _, _, way_of_deliveries = self.http_client.get("/wayofdeliveries", params=params)
        return way_of_deliveries

    def retrieve(self, code):
        """
        Retrieve a single WayOfDelivery

        Returns a single WayOfDelivery according to the unique WayOfDelivery ID provided
        If the specified WayOfDelivery does not exist, this query returns an error

        :calls: ``get /wayofdeliveries/{code}``
        :param int id: Unique identifier of a WayOfDelivery.
        :return: Dictionary that support attriubte-style access and represent WayOfDelivery resource.
        :rtype: dict
        """
        _, _, way_of_delivery = self.http_client.get("/wayofdeliveries/{code}".format(code=code))
        return way_of_delivery

    def create(self, *args, **kwargs):
        """
        Create a WayOfDelivery

        Creates a new WayOfDelivery
        **Notice** the WayOfDelivery's name **must** be unique within the scope of the resource_type

        :calls: ``post /wayofdeliveries``
        :param tuple *args: (optional) Single object representing WayOfDelivery resource.
        :param dict **kwargs: (optional) way_of_delivery attributes.
        :return: Dictionary that support attriubte-style access and represents newely created WayOfDelivery resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for WayOfDelivery are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, way_of_delivery = self.http_client.post("/wayofdeliveries", body=attributes)
        return way_of_delivery

    def update(self, code, *args, **kwargs):
        """
        Update a WayOfDelivery

        Updates a WayOfDelivery's information
        If the specified WayOfDelivery does not exist, this query will return an error
        **Notice** if you want to update a WayOfDelivery, you **must** make sure the WayOfDelivery's name is unique within the scope of the specified resource

        :calls: ``put /wayofdeliveries/{code}``
        :param int id: Unique identifier of a WayOfDelivery.
        :param tuple *args: (optional) Single object representing WayOfDelivery resource which attributes should be updated.
        :param dict **kwargs: (optional) WayOfDelivery attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated WayOfDelivery resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for WayOfDelivery are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, way_of_delivery = self.http_client.put("/wayofdeliveries/{code}".format(code=code), body=attributes)
        return way_of_delivery

    def destroy(self, code):
        """
        Delete a WayOfDelivery

        Deletes an existing WayOfDelivery
        If the specified WayOfDelivery is assigned to any resource, we will remove this WayOfDelivery from all such resources
        If the specified WayOfDelivery does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /wayofdeliveries/{code}``
        :param int id: Unique identifier of a WayOfDelivery.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/wayofdeliveries/{code}".format(code=code))
        return status_code == 204
