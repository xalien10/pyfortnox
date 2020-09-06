class PriceListService(object):
    """
    :class:`fortnox.PriceListService` is used by :class:`fortnox.Client` to make
    actions related to PriceList resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for PriceList to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Code', 'Description', 'Comments', 'PreSelected']
    SERVICE = "PriceList"

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
        Retrieve all PriceList

        Returns all PriceList available to the Company, according to the parameters provided

        :calls: ``get /pricelists``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of PriceList.
        :rtype: list
        """

        _, _, price_lists = self.http_client.get("/pricelists", params=params)
        return price_lists

    def retrieve(self, code):
        """
        Retrieve a single PriceList

        Returns a single PriceList according to the unique PriceList ID provided
        If the specified PriceList does not exist, this query returns an error

        :calls: ``get /pricelists/{code}``
        :param int id: Unique identifier of a PriceList.
        :return: Dictionary that support attriubte-style access and represent PriceList resource.
        :rtype: dict
        """
        _, _, price_list = self.http_client.get("/pricelists/{code}".format(code=code))
        return price_list

    def create(self, *args, **kwargs):
        """
        Create a PriceList

        Creates a new PriceList
        **Notice** the PriceList's name **must** be unique within the scope of the resource_type

        :calls: ``post /pricelists``
        :param tuple *args: (optional) Single object representing PriceList resource.
        :param dict **kwargs: (optional) price_list attributes.
        :return: Dictionary that support attriubte-style access and represents newely created PriceList resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for PriceList are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, price_list = self.http_client.post("/pricelists", body=attributes)
        return price_list

    def update(self, code, *args, **kwargs):
        """
        Update a PriceList

        Updates a PriceList's information
        If the specified PriceList does not exist, this query will return an error
        **Notice** if you want to update a PriceList, you **must** make sure the PriceList's name is unique within the scope of the specified resource

        :calls: ``put /pricelists/{code}``
        :param int id: Unique identifier of a PriceList.
        :param tuple *args: (optional) Single object representing PriceList resource which attributes should be updated.
        :param dict **kwargs: (optional) PriceList attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated PriceList resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for PriceList are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, price_list = self.http_client.put("/pricelists/{code}".format(code=code), body=attributes)
        return price_list
