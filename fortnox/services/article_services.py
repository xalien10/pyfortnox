class ArticleService(object):
    """
    :class:`fortnox.ArticleService` is used by :class:`fortnox.Client` to make
    actions related to Articles resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Articles to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['ArticleNumber', 'Description']
    SERVICE = "Article"

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
        Retrieve all Articles

        Returns all Articles available to the Company, according to the parameters provided

        :calls: ``get /articles``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Articles.
        :rtype: list
        """

        _, _, articles = self.http_client.get("/articles", params=params)
        return articles

    def retrieve(self, number):
        """
        Retrieve a single Article

        Returns a single Article according to the unique Article ID provided
        If the specified Article does not exist, this query returns an error

        :calls: ``get /articles/{number}``
        :param int id: Unique identifier of an Article.
        :return: Dictionary that support attriubte-style access and represent Article resource.
        :rtype: dict
        """
        _, _, article = self.http_client.get("/articles/{number}".format(number=number))
        return article

    def create(self, *args, **kwargs):
        """
        Create an Article

        Creates a new Article
        **Notice** the Article's name **must** be unique within the scope of the resource_type

        :calls: ``post /articles``
        :param tuple *args: (optional) Single object representing Article resource.
        :param dict **kwargs: (optional) Article attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Articles resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Article are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items() if k in self.OPTS_KEYS_TO_PERSIST)
        attributes.update({'service': self.SERVICE})
        _, _, article = self.http_client.post("/articles", body=attributes)
        return article

    def update(self, number, *args, **kwargs):
        """
        Update an Article

        Updates an Article's information
        If the specified Article does not exist, this query will return an error
        **Notice** if you want to update an Article, you **must** make sure the Article's name is unique within the scope of the specified resource

        :calls: ``put /articles/{number}``
        :param int id: Unique identifier of an Article.
        :param tuple *args: (optional) Single object representing Article resource which attributes should be updated.
        :param dict **kwargs: (optional) Article attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Article resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Article are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, article = self.http_client.put("/articles/{number}".format(number=number), body=attributes)
        return article

    def destroy(self, number):
        """
        Delete an Article

        Deletes an existing Article
        If the specified Article is assigned to any resource, we will remove this Article from all such resources
        If the specified Article does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /articles/{number}``
        :param int id: Unique identifier of an Article.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/articles/{number}".format(number=number))
        return status_code == 204
