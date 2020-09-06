class ArchiveService(object):
    """
    :class:`fortnox.ArchiveService` is used by :class:`fortnox.Client` to make
    actions related to ArchiveService resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for ArchiveService to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Name']
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
        Retrieve all Archives

        Returns all ArchiveService available to the Company, according to the parameters provided

        :calls: ``get /archive``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Archives.
        :rtype: list
        """

        _, _, archives = self.http_client.get("/archive", params=params)
        return archives

    def retrieve(self, id):
        """
        Retrieve a single ArchiveService

        Returns a single ArchiveService according to the unique ArchiveService ID provided
        If the specified ArchiveService does not exist, this query returns an error

        :calls: ``get /archive/{id}``
        :param int id: Unique identifier of a ArchiveService.
        :return: Dictionary that support attriubte-style access and represent ArchiveService resource.
        :rtype: dict
        """
        _, _, archive = self.http_client.get("/archive/{id}".format(id=id))
        return archive

    def create(self, *args, **kwargs):
        """
        Create a ArchiveService

        Creates a new customer
        **Notice** the customer's name **must** be unique within the scope of the resource_type

        :calls: ``post /archive``
        :param tuple *args: (optional) Single object representing ArchiveService resource.
        :param dict **kwargs: (optional) Customer attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Customer resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for ArchiveService are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, archive = self.http_client.post("/archive", body=attributes)
        return archive

    def destroy(self, id):
        """
        Delete a ArchiveService

        Deletes an existing ArchiveService
        If the specified ArchiveService is assigned to any resource, we will remove this ArchiveService from all such resources
        If the specified ArchiveService does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /archive/{id}``
        :param int id: Unique identifier of a ArchiveService.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/archive/{id}".format(id=id))
        return status_code == 204
