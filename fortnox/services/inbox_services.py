class InboxService(object):
    """
    :class:`fortnox.InboxService` is used by :class:`fortnox.Client` to make
    actions related to Inbox resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Inbox to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Name', 'Id']
    SERVICE = "Folder"

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
        Retrieve all Inbox

        Returns all Inbox available to the Company, according to the parameters provided

        :calls: ``get /inbox``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Inbox.
        :rtype: list
        """

        _, _, folders = self.http_client.get("/inbox", params=params)
        return folders

    def retrieve(self, id):
        """
        Retrieve a single Inbox

        Returns a single Inbox according to the unique Inbox ID provided
        If the specified Inbox does not exist, this query returns an error

        :calls: ``get /inbox/{id}``
        :param int id: Unique identifier of a Inbox.
        :return: Dictionary that support attriubte-style access and represent Inbox resource.
        :rtype: dict
        """
        _, _, folder = self.http_client.get("/inbox/{id}".format(id=id))
        return folder

    def create(self, *args, **kwargs):
        """
        Create a Inbox

        Creates a new Inbox
        **Notice** the Inbox's name **must** be unique within the scope of the resource_type

        :calls: ``post /inbox``
        :param tuple *args: (optional) Single object representing Inbox resource.
        :param dict **kwargs: (optional) folder attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Inbox resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Inbox are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items() if k in self.OPTS_KEYS_TO_PERSIST)
        attributes.update({'service': self.SERVICE})
        _, _, folder = self.http_client.post("/inbox", body=attributes)
        return folder

    def update(self, id, *args, **kwargs):
        """
        Update a Inbox

        Updates a Inbox's information
        If the specified Inbox does not exist, this query will return an error
        **Notice** if you want to update a Inbox, you **must** make sure the Inbox's name is unique within the scope of the specified resource

        :calls: ``put /inbox/{id}``
        :param int id: Unique identifier of a Inbox.
        :param tuple *args: (optional) Single object representing Inbox resource which attributes should be updated.
        :param dict **kwargs: (optional) Inbox attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Inbox resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Inbox are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, folder = self.http_client.put("/inbox/{id}".format(id=id), body=attributes)
        return folder

    def destroy(self, id):
        """
        Delete a Inbox

        Deletes an existing Inbox
        If the specified Inbox is assigned to any resource, we will remove this Inbox from all such resources
        If the specified Inbox does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /inbox/{id}``
        :param int id: Unique identifier of a Inbox.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/inbox/{id}".format(id=id))
        return status_code == 204
