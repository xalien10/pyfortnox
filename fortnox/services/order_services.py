class OrderService(object):
    """
    :class:`fortnox.OrderService` is used by :class:`fortnox.Client` to make
    actions related to Order resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Order to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['CustomerNumber', 'OrderRows']

    """
    OrderRows has the following structures:
        "OrderRows": [
          {
            "ArticleNumber": "11",
            "DeliveredQuantity": "10",
            "Description": "Trycksak: 4 sid A4",
            "OrderedQuantity": "10",
            "Unit": "st"
          },
          {
            "ArticleNumber": "12",
            "DeliveredQuantity": "10",
            "Description": "Trycksak: 4 sid A4",
            "OrderedQuantity": "10",
            "Unit": "st"
          },
          ..................
        ]
    """

    SERVICE = "Order"

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
        Retrieve all Order

        Returns all Order available to the Company, according to the parameters provided

        :calls: ``get /orders``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Order.
        :rtype: list
        """

        _, _, orders = self.http_client.get("/orders", params=params)
        return orders

    def retrieve(self, document_number):
        """
        Retrieve a single Order

        Returns a single Order according to the unique Order ID provided
        If the specified Order does not exist, this query returns an error

        :calls: ``get /orders/{document_number}``
        :param int id: Unique identifier of a Order.
        :return: Dictionary that support attriubte-style access and represent Order resource.
        :rtype: dict
        """
        _, _, order = self.http_client.get("/orders/{document_number}".format(document_number=document_number))
        return order

    def create(self, *args, **kwargs):
        """
        Create a Order

        Creates a new Order
        **Notice** the Order's name **must** be unique within the scope of the resource_type

        :calls: ``post /orders``
        :param tuple *args: (optional) Single object representing Order resource.
        :param dict **kwargs: (optional) order attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Order resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Order are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, order = self.http_client.post("/orders", body=attributes)
        return order

    def update(self, document_number, *args, **kwargs):
        """
        Update a Order

        Updates a Order's information
        If the specified Order does not exist, this query will return an error
        **Notice** if you want to update a Order, you **must** make sure the Order's name is unique within the scope of the specified resource

        :calls: ``put /orders/{document_number}``
        :param int id: Unique identifier of a Order.
        :param tuple *args: (optional) Single object representing Order resource which attributes should be updated.
        :param dict **kwargs: (optional) Order attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Order resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Order are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, order = self.http_client.put("/orders/{document_number}".format(document_number=document_number),
                                           body=attributes)
        return order
