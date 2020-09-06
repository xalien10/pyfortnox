class LabelService(object):
    """
    :class:`fortnox.LabelService` is used by :class:`fortnox.Client` to make
    actions related to Label resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Label to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Description']
    SERVICE = "Label"

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
        Retrieve all Label

        Returns all Label available to the Company, according to the parameters provided

        :calls: ``get /labels``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Label.
        :rtype: list
        """

        _, _, labels = self.http_client.get("/labels", params=params)
        return labels

    def retrieve(self, id):
        """
        Retrieve a single Label

        Returns a single Label according to the unique Label ID provided
        If the specified Label does not exist, this query returns an error

        :calls: ``get /labels/{id}``
        :param int id: Unique identifier of a Label.
        :return: Dictionary that support attriubte-style access and represent Label resource.
        :rtype: dict
        """
        _, _, label = self.http_client.get("/labels/{id}".format(id=id))
        return label

    def create(self, *args, **kwargs):
        """
        Create a Label

        Creates a new Label
        **Notice** the Label's name **must** be unique within the scope of the resource_type

        :calls: ``post /labels``
        :param tuple *args: (optional) Single object representing Label resource.
        :param dict **kwargs: (optional) label attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Label resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Label are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, label = self.http_client.post("/labels", body=attributes)
        return label

    def update(self, id, *args, **kwargs):
        """
        Update a Label

        Updates a Label's information
        If the specified Label does not exist, this query will return an error
        **Notice** if you want to update a Label, you **must** make sure the Label's name is unique within the scope of the specified resource

        :calls: ``put /labels/{id}``
        :param int id: Unique identifier of a Label.
        :param tuple *args: (optional) Single object representing Label resource which attributes should be updated.
        :param dict **kwargs: (optional) Label attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Label resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Label are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, label = self.http_client.put("/labels/{id}".format(id=id), body=attributes)
        return label

    def destroy(self, id):
        """
        Delete a Label

        Deletes an existing Label
        If the specified Label is assigned to any resource, we will remove this Label from all such resources
        If the specified Label does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /labels/{id}``
        :param int id: Unique identifier of a Label.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/labels/{id}".format(id=id))
        return status_code == 204
