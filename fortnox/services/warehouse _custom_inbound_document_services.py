class Service(object):
    """
    :class:`fortnox.<specific-service>` is used by :class:`fortnox.Client` to make
    actions related to <specific-service> resource.

    Normally you won't instantiate this class directly.
    Warehouse related operations root url is different
    """
    # TODO: Need to implement exceptionally

    """
    Allowed attributes for <specific-service> to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Name']
    SERVICE = "<specific-service>"

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
        Retrieve all <specific-service>

        Returns all <specific-service> available to the Company, according to the parameters provided

        :calls: ``get /<specific-service-path>``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of <specific-service>.
        :rtype: list
        """

        _, _, customers = self.http_client.get("/<specific-service-path>", params=params)
        return customers

    def retrieve(self, id):
        """
        Retrieve a single <specific-service>

        Returns a single <specific-service> according to the unique <specific-service> ID provided
        If the specified <specific-service> does not exist, this query returns an error

        :calls: ``get /<specific-service-path>/{id}``
        :param int id: Unique identifier of a <specific-service>.
        :return: Dictionary that support attriubte-style access and represent <specific-service> resource.
        :rtype: dict
        """
        _, _, customer = self.http_client.get("/<specific-service-path>/{id}".format(id=id))
        return customer

    def create(self, *args, **kwargs):
        """
        Create a <specific-service>

        Creates a new <specific-service>
        **Notice** the <specific-service>'s name **must** be unique within the scope of the resource_type

        :calls: ``post /<specific-service-path>``
        :param tuple *args: (optional) Single object representing <specific-service> resource.
        :param dict **kwargs: (optional) Customer attributes.
        :return: Dictionary that support attriubte-style access and represents newely created <specific-service> resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for <specific-service> are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items() if k in self.OPTS_KEYS_TO_PERSIST)
        attributes.update({'service': self.SERVICE})
        _, _, customer = self.http_client.post("/<specific-service-path>", body=attributes)
        return customer

    def update(self, id, *args, **kwargs):
        """
        Update a <specific-service>

        Updates a <specific-service>'s information
        If the specified <specific-service> does not exist, this query will return an error
        **Notice** if you want to update a <specific-service>, you **must** make sure the <specific-service>'s name is unique within the scope of the specified resource

        :calls: ``put /<specific-service-path>/{id}``
        :param int id: Unique identifier of a <specific-service>.
        :param tuple *args: (optional) Single object representing <specific-service> resource which attributes should be updated.
        :param dict **kwargs: (optional) <specific-service> attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated <specific-service> resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for <specific-service> are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, customer = self.http_client.put("/<specific-service-path>/{id}".format(id=id), body=attributes)
        return customer

    def destroy(self, id):
        """
        Delete a <specific-service>

        Deletes an existing <specific-service>
        If the specified <specific-service> is assigned to any resource, we will remove this <specific-service> from all such resources
        If the specified <specific-service> does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /<specific-service-path>/{id}``
        :param int id: Unique identifier of a <specific-service>.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/<specific-service-path>/{id}".format(id=id))
        return status_code == 204
