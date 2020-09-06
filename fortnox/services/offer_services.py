class OfferService(object):
    """
    :class:`fortnox.OfferService` is used by :class:`fortnox.Client` to make
    actions related to Offer resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Offer to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['CustomerNumber', 'OfferRows']

    """
    OfferRows has the following structures:
        "OfferRows": [
          {
            "ArticleNumber": "1",
            "Quantity": "3.00",
            "AccountNumber": "3011"
          },
          {
            "ArticleNumber": "2",
            "Quantity": "7.00",
            "AccountNumber": "3011"
          },
          ................
        ]
    """

    SERVICE = "Offer"

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
        Retrieve all Offer

        Returns all Offer available to the Company, according to the parameters provided

        :calls: ``get /offers``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Offer.
        :rtype: list
        """

        _, _, offers = self.http_client.get("/offers", params=params)
        return offers

    def retrieve(self, document_number):
        """
        Retrieve a single Offer

        Returns a single Offer according to the unique Offer ID provided
        If the specified Offer does not exist, this query returns an error

        :calls: ``get /offers/{document_number}``
        :param int id: Unique identifier of a Offer.
        :return: Dictionary that support attriubte-style access and represent Offer resource.
        :rtype: dict
        """
        _, _, offer = self.http_client.get("/offers/{document_number}".format(document_number=document_number))
        return offer

    def create(self, *args, **kwargs):
        """
        Create a Offer

        Creates a new Offer
        **Notice** the Offer's name **must** be unique within the scope of the resource_type

        :calls: ``post /offers``
        :param tuple *args: (optional) Single object representing Offer resource.
        :param dict **kwargs: (optional) offer attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Offer resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Offer are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, offer = self.http_client.post("/offers", body=attributes)
        return offer

    def update(self, document_number, *args, **kwargs):
        """
        Update a Offer

        Updates a Offer's information
        If the specified Offer does not exist, this query will return an error
        **Notice** if you want to update a Offer, you **must** make sure the Offer's name is unique within the scope of the specified resource

        :calls: ``put /offers/{document_number}``
        :param int id: Unique identifier of a Offer.
        :param tuple *args: (optional) Single object representing Offer resource which attributes should be updated.
        :param dict **kwargs: (optional) Offer attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Offer resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Offer are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, offer = self.http_client.put("/offers/{document_number}".format(document_number=document_number),
                                           body=attributes)
        return offer
