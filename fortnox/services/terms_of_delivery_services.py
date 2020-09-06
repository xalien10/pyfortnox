class TermsOfDeliveryService(object):
    """
    :class:`fortnox.TermsOfDeliveryService` is used by :class:`fortnox.Client` to make
    actions related to TermsOfDelivery resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for TermsOfDelivery to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Code', 'Description']
    SERVICE = "TermsOfDelivery"

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
        Retrieve all TermsOfDelivery

        Returns all TermsOfDelivery available to the Company, according to the parameters provided

        :calls: ``get /termsofdeliveries``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of TermsOfDelivery.
        :rtype: list
        """

        _, _, terms_of_deliveries = self.http_client.get("/termsofdeliveries", params=params)
        return terms_of_deliveries

    def retrieve(self, code):
        """
        Retrieve a single TermsOfDelivery

        Returns a single TermsOfDelivery according to the unique TermsOfDelivery ID provided
        If the specified TermsOfDelivery does not exist, this query returns an error

        :calls: ``get /termsofdeliveries/{code}``
        :param int id: Unique identifier of a TermsOfDelivery.
        :return: Dictionary that support attriubte-style access and represent TermsOfDelivery resource.
        :rtype: dict
        """
        _, _, terms_of_delivery = self.http_client.get("/termsofdeliveries/{code}".format(code=code))
        return terms_of_delivery

    def create(self, *args, **kwargs):
        """
        Create a TermsOfDelivery

        Creates a new TermsOfDelivery
        **Notice** the TermsOfDelivery's name **must** be unique within the scope of the resource_type

        :calls: ``post /termsofdeliveries``
        :param tuple *args: (optional) Single object representing TermsOfDelivery resource.
        :param dict **kwargs: (optional) terms_of_delivery attributes.
        :return: Dictionary that support attriubte-style access and represents newely created TermsOfDelivery resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for TermsOfDelivery are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, terms_of_delivery = self.http_client.post("/termsofdeliveries", body=attributes)
        return terms_of_delivery

    def update(self, code, *args, **kwargs):
        """
        Update a TermsOfDelivery

        Updates a TermsOfDelivery's information
        If the specified TermsOfDelivery does not exist, this query will return an error
        **Notice** if you want to update a TermsOfDelivery, you **must** make sure the TermsOfDelivery's name is unique within the scope of the specified resource

        :calls: ``put /termsofdeliveries/{code}``
        :param int id: Unique identifier of a TermsOfDelivery.
        :param tuple *args: (optional) Single object representing TermsOfDelivery resource which attributes should be updated.
        :param dict **kwargs: (optional) TermsOfDelivery attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated TermsOfDelivery resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for TermsOfDelivery are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, terms_of_delivery = self.http_client.put("/termsofdeliveries/{code}".format(code=code), body=attributes)
        return terms_of_delivery
