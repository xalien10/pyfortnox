class CostCenterService(object):
    """
    :class:`fortnox.CostCenterService` is used by :class:`fortnox.Client` to make
    actions related to CostCenter resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for CostCenter to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Code', 'Description']
    SERVICE = "CostCenter"

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
        Retrieve all CostCenter

        Returns all CostCenter available to the Company, according to the parameters provided

        :calls: ``get /costcenters``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of CostCenter.
        :rtype: list
        """

        _, _, cost_centers = self.http_client.get("/costcenters", params=params)
        return cost_centers

    def retrieve(self, code):
        """
        Retrieve a single CostCenter

        Returns a single CostCenter according to the unique CostCenter ID provided
        If the specified CostCenter does not exist, this query returns an error

        :calls: ``get /costcenters/{code}``
        :param int id: Unique identifier of a CostCenter.
        :return: Dictionary that support attriubte-style access and represent CostCenter resource.
        :rtype: dict
        """
        _, _, cost_center = self.http_client.get("/costcenters/{code}".format(code=code))
        return cost_center

    def create(self, *args, **kwargs):
        """
        Create a CostCenter

        Creates a new CostCenter
        **Notice** the CostCenter's name **must** be unique within the scope of the resource_type

        :calls: ``post /costcenters``
        :param tuple *args: (optional) Single object representing CostCenter resource.
        :param dict **kwargs: (optional) cost_center attributes.
        :return: Dictionary that support attriubte-style access and represents newely created CostCenter resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for CostCenter are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, cost_center = self.http_client.post("/costcenters", body=attributes)
        return cost_center

    def update(self, code, *args, **kwargs):
        """
        Update a CostCenter

        Updates a CostCenter's information
        If the specified CostCenter does not exist, this query will return an error
        **Notice** if you want to update a CostCenter, you **must** make sure the CostCenter's name is unique within the scope of the specified resource

        :calls: ``put /costcenters/{code}``
        :param int id: Unique identifier of a CostCenter.
        :param tuple *args: (optional) Single object representing CostCenter resource which attributes should be updated.
        :param dict **kwargs: (optional) CostCenter attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated CostCenter resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for CostCenter are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, cost_center = self.http_client.put("/costcenters/{code}".format(code=code), body=attributes)
        return cost_center

    def destroy(self, code):
        """
        Delete a CostCenter

        Deletes an existing CostCenter
        If the specified CostCenter is assigned to any resource, we will remove this CostCenter from all such resources
        If the specified CostCenter does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /costcenters/{code}``
        :param int id: Unique identifier of a CostCenter.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/costcenters/{code}".format(code=code))
        return status_code == 204
