class TaxReductionService(object):
    """
    :class:`fortnox.TaxReductionService` is used by :class:`fortnox.Client` to make
    actions related to TaxReduction resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for TaxReduction to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['AskedAmount', 'CustomerName', 'ReferenceDocumentType',
                            'ReferenceNumber', 'SocialSecurityNumber']
    SERVICE = "TaxReduction"

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
        Retrieve all TaxReduction

        Returns all TaxReduction available to the Company, according to the parameters provided

        :calls: ``get /taxreductions``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of TaxReduction.
        :rtype: list
        """

        _, _, tax_reductions = self.http_client.get("/taxreductions", params=params)
        return tax_reductions

    def retrieve(self, id):
        """
        Retrieve a single TaxReduction

        Returns a single TaxReduction according to the unique TaxReduction ID provided
        If the specified TaxReduction does not exist, this query returns an error

        :calls: ``get /taxreductions/{id}``
        :param int id: Unique identifier of a TaxReduction.
        :return: Dictionary that support attriubte-style access and represent TaxReduction resource.
        :rtype: dict
        """
        _, _, tax_reduction = self.http_client.get("/taxreductions/{id}".format(id=id))
        return tax_reduction

    def create(self, *args, **kwargs):
        """
        Create a TaxReduction

        Creates a new TaxReduction
        **Notice** the TaxReduction's name **must** be unique within the scope of the resource_type

        :calls: ``post /taxreductions``
        :param tuple *args: (optional) Single object representing TaxReduction resource.
        :param dict **kwargs: (optional) tax_reduction attributes.
        :return: Dictionary that support attriubte-style access and represents newely created TaxReduction resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for TaxReduction are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, tax_reduction = self.http_client.post("/taxreductions", body=attributes)
        return tax_reduction

    def update(self, id, *args, **kwargs):
        """
        Update a TaxReduction

        Updates a TaxReduction's information
        If the specified TaxReduction does not exist, this query will return an error
        **Notice** if you want to update a TaxReduction, you **must** make sure the TaxReduction's name is unique within the scope of the specified resource

        :calls: ``put /taxreductions/{id}``
        :param int id: Unique identifier of a TaxReduction.
        :param tuple *args: (optional) Single object representing TaxReduction resource which attributes should be updated.
        :param dict **kwargs: (optional) TaxReduction attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated TaxReduction resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for TaxReduction are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, tax_reduction = self.http_client.put("/taxreductions/{id}".format(id=id), body=attributes)
        return tax_reduction

    def destroy(self, id):
        """
        Delete a TaxReduction

        Deletes an existing TaxReduction
        If the specified TaxReduction is assigned to any resource, we will remove this TaxReduction from all such resources
        If the specified TaxReduction does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /taxreductions/{id}``
        :param int id: Unique identifier of a TaxReduction.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/taxreductions/{id}".format(id=id))
        return status_code == 204
