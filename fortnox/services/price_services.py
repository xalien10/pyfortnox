class PriceService(object):
    """
    :class:`fortnox.PriceService` is used by :class:`fortnox.Client` to make
    actions related to Price resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Price to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['ArticleNumber', 'FromQuantity', 'Price', 'PriceList']
    SERVICE = "Price"

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
        Retrieve all Price

        Returns all Price available to the Company, according to the parameters provided

        :calls: ``get /prices``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Price.
        :rtype: list
        """
        # TODO: Need to properly implement it

        _, _, prices = self.http_client.get("/prices", params=params)
        return prices

    def retrieve_sublist(self, price_list, article_number):
        """
        Retrieve a sublist of a Price list

        Returns a single Price according to the unique Price ID provided
        If the specified Price does not exist, this query returns an error

        :calls: ``get /prices/{price_list}/{article_number}/{from_quantity}``
        :param int id: Unique identifier of a Price.
        :return: Dictionary that support attriubte-style access and represent Price resource.
        :rtype: dict
        """
        _, _, price_sublist = self.http_client.get(
            "/prices/{price_list}/{article_number}".format(price_list=price_list, article_number=article_number))
        return price_sublist

    def retrieve(self, price_list, article_number, from_quantity):
        """
        Retrieve a single Price

        Returns a single Price according to the unique Price ID provided
        If the specified Price does not exist, this query returns an error

        :calls: ``get /prices/{price_list}/{article_number}/{from_quantity}``
        :param int id: Unique identifier of a Price.
        :return: Dictionary that support attriubte-style access and represent Price resource.
        :rtype: dict
        """
        _, _, price = self.http_client.get(
            "/prices/{price_list}/{article_number}/{from_quantity}".format(price_list=price_list,
                                                                           article_number=article_number,
                                                                           from_quantity=from_quantity))
        return price

    def create(self, *args, **kwargs):
        """
        Create a Price

        Creates a new Price
        **Notice** the Price's name **must** be unique within the scope of the resource_type

        :calls: ``post /prices``
        :param tuple *args: (optional) Single object representing Price resource.
        :param dict **kwargs: (optional) price attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Price resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Price are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, price = self.http_client.post("/prices", body=attributes)
        return price

    def update(self, price_list, article_number, from_quantity, *args, **kwargs):
        """
        Update a Price

        Updates a Price's information
        If the specified Price does not exist, this query will return an error
        **Notice** if you want to update a Price, you **must** make sure the Price's name is unique within the scope of the specified resource

        :calls: ``put /prices/{price_list}/{article_number}/{from_quantity}``
        :param int id: Unique identifier of a Price.
        :param tuple *args: (optional) Single object representing Price resource which attributes should be updated.
        :param dict **kwargs: (optional) Price attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Price resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Price are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, price = self.http_client.put(
            "/prices/{price_list}/{article_number}/{from_quantity}".format(price_list=price_list,
                                                                           article_number=article_number,
                                                                           from_quantity=from_quantity),
            body=attributes)
        return price

    def destroy(self, price_list, article_number, from_quantity):
        """
        Delete a Price

        Deletes an existing Price
        If the specified Price is assigned to any resource, we will remove this Price from all such resources
        If the specified Price does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /prices/{price_list}/{article_number}/{from_quantity}``
        :param int id: Unique identifier of a Price.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete(
            "/prices/{price_list}/{article_number}/{from_quantity}".format(price_list=price_list,
                                                                           article_number=article_number,
                                                                           from_quantity=from_quantity))
        return status_code == 204
