class ArticleFileConnectionsService(object):
    """
    :class:`fortnox.ArticleFileConnectionsService` is used by :class:`fortnox.Client` to make
    actions related to ArticleFileConnections resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for ArticleFileConnections to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['FileId', 'ArticleNumber']
    SERVICE = "ArticleFileConnection"

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
        Retrieve all ArticleFileConnections

        Returns all ArticleFileConnections available to the Company, according to the parameters provided

        :calls: ``get /articlefileconnections``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Customers.
        :rtype: list
        """

        _, _, article_file_connections = self.http_client.get("/articlefileconnections", params=params)
        return article_file_connections

    def retrieve(self, file_id):
        """
        Retrieve a single ArticleFileConnections

        Returns a single ArticleFileConnections according to the unique ArticleFileConnections ID provided
        If the specified ArticleFileConnections does not exist, this query returns an error

        :calls: ``get /articlefileconnections/{file_id}``
        :param int id: Unique identifier of a ArticleFileConnections.
        :return: Dictionary that support attriubte-style access and represent ArticleFileConnections resource.
        :rtype: dict
        """
        _, _, article_file_connection = self.http_client.get(
            "/articlefileconnections/{file_id}".format(file_id=file_id))
        return article_file_connection

    def create(self, *args, **kwargs):
        """
        Create a ArticleFileConnections

        Creates a new customer
        **Notice** the customer's name **must** be unique within the scope of the resource_type

        :calls: ``post /articlefileconnections``
        :param tuple *args: (optional) Single object representing ArticleFileConnections resource.
        :param dict **kwargs: (optional) Customer attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Customer resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for ArticleFileConnections are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, article_file_connection = self.http_client.post("/articlefileconnections", body=attributes)
        return article_file_connection

    def destroy(self, file_id):
        """
        Delete a ArticleFileConnections

        Deletes an existing ArticleFileConnections
        If the specified ArticleFileConnections is assigned to any resource, we will remove this ArticleFileConnections from all such resources
        If the specified ArticleFileConnections does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /articlefileconnections/{file_id}``
        :param int id: Unique identifier of a ArticleFileConnections.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/articlefileconnections/{file_id}".format(file_id=file_id))
        return status_code == 204
