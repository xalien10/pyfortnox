class TermsOfPaymentService(object):
    """
    :class:`fortnox.TermsOfPaymentService` is used by :class:`fortnox.Client` to make
    actions related to TermsOfPayment resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for TermsOfPayment to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Code', 'Description']
    SERVICE = "TermsOfPayment"

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
        Retrieve all TermsOfPayment

        Returns all TermsOfPayment available to the Company, according to the parameters provided

        :calls: ``get /termsofpayments``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of TermsOfPayment.
        :rtype: list
        """

        _, _, terms_of_payments = self.http_client.get("/termsofpayments", params=params)
        return terms_of_payments

    def retrieve(self, code):
        """
        Retrieve a single TermsOfPayment

        Returns a single TermsOfPayment according to the unique TermsOfPayment ID provided
        If the specified TermsOfPayment does not exist, this query returns an error

        :calls: ``get /termsofpayments/{code}``
        :param int id: Unique identifier of a TermsOfPayment.
        :return: Dictionary that support attriubte-style access and represent TermsOfPayment resource.
        :rtype: dict
        """
        _, _, terms_of_payment = self.http_client.get("/termsofpayments/{code}".format(code=code))
        return terms_of_payment

    def create(self, *args, **kwargs):
        """
        Create a TermsOfPayment

        Creates a new TermsOfPayment
        **Notice** the TermsOfPayment's name **must** be unique within the scope of the resource_type

        :calls: ``post /termsofpayments``
        :param tuple *args: (optional) Single object representing TermsOfPayment resource.
        :param dict **kwargs: (optional) terms_of_payment attributes.
        :return: Dictionary that support attriubte-style access and represents newely created TermsOfPayment resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for TermsOfPayment are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, terms_of_payment = self.http_client.post("/termsofpayments", body=attributes)
        return terms_of_payment

    def update(self, code, *args, **kwargs):
        """
        Update a TermsOfPayment

        Updates a TermsOfPayment's information
        If the specified TermsOfPayment does not exist, this query will return an error
        **Notice** if you want to update a TermsOfPayment, you **must** make sure the TermsOfPayment's name is unique within the scope of the specified resource

        :calls: ``put /termsofpayments/{code}``
        :param int id: Unique identifier of a TermsOfPayment.
        :param tuple *args: (optional) Single object representing TermsOfPayment resource which attributes should be updated.
        :param dict **kwargs: (optional) TermsOfPayment attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated TermsOfPayment resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for TermsOfPayment are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, terms_of_payment = self.http_client.put("/termsofpayments/{code}".format(code=code), body=attributes)
        return terms_of_payment

    def destroy(self, code):
        """
        Delete a TermsOfPayment

        Deletes an existing TermsOfPayment
        If the specified TermsOfPayment is assigned to any resource, we will remove this TermsOfPayment from all such resources
        If the specified TermsOfPayment does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /termsofpayments/{code}``
        :param int id: Unique identifier of a TermsOfPayment.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/termsofpayments/{code}".format(code=code))
        return status_code == 204
