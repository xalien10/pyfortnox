class ModesOfPaymentService(object):
    """
    :class:`fortnox.ModesOfPaymentService` is used by :class:`fortnox.Client` to make
    actions related to ModesOfPayment resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for ModesOfPayment to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Code', 'Description']
    SERVICE = "ModesOfPayment"

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
        Retrieve all ModesOfPayment

        Returns all ModesOfPayment available to the Company, according to the parameters provided

        :calls: ``get /modesofpayments``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of ModesOfPayment.
        :rtype: list
        """

        _, _, modes_of_payments = self.http_client.get("/modesofpayments", params=params)
        return modes_of_payments

    def retrieve(self, code):
        """
        Retrieve a single ModesOfPayment

        Returns a single ModesOfPayment according to the unique ModesOfPayment ID provided
        If the specified ModesOfPayment does not exist, this query returns an error

        :calls: ``get /modesofpayments/{code}``
        :param int id: Unique identifier of a ModesOfPayment.
        :return: Dictionary that support attriubte-style access and represent ModesOfPayment resource.
        :rtype: dict
        """
        _, _, modes_of_payment = self.http_client.get("/modesofpayments/{code}".format(code=code))
        return modes_of_payment

    def create(self, *args, **kwargs):
        """
        Create a ModesOfPayment

        Creates a new ModesOfPayment
        **Notice** the ModesOfPayment's name **must** be unique within the scope of the resource_type

        :calls: ``post /modesofpayments``
        :param tuple *args: (optional) Single object representing ModesOfPayment resource.
        :param dict **kwargs: (optional) modes_of_payment attributes.
        :return: Dictionary that support attriubte-style access and represents newely created ModesOfPayment resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for ModesOfPayment are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, modes_of_payment = self.http_client.post("/modesofpayments", body=attributes)
        return modes_of_payment

    def update(self, code, *args, **kwargs):
        """
        Update a ModesOfPayment

        Updates a ModesOfPayment's information
        If the specified ModesOfPayment does not exist, this query will return an error
        **Notice** if you want to update a ModesOfPayment, you **must** make sure the ModesOfPayment's name is unique within the scope of the specified resource

        :calls: ``put /modesofpayments/{code}``
        :param int id: Unique identifier of a ModesOfPayment.
        :param tuple *args: (optional) Single object representing ModesOfPayment resource which attributes should be updated.
        :param dict **kwargs: (optional) ModesOfPayment attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated ModesOfPayment resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for ModesOfPayment are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, modes_of_payment = self.http_client.put("/modesofpayments/{code}".format(code=code), body=attributes)
        return modes_of_payment
