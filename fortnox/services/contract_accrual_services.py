class ContractAccrualService(object):
    """
    :class:`fortnox.ContractAccrualService` is used by :class:`fortnox.Client` to make
    actions related to ContractAccruals resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for ContractAccruals to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['AccrualAccount', 'CostAccount', 'AccrualRows']
    """
    AccuralRows will have following structures
        "AccrualRows": [
          {
            "Account": <account_number>,
            "Credit": amount,
            "Debit": amount
          },
          {
            "Account": <account_number>,
            "Credit": amount,
            "Debit": amount
          },
          ........
        ]
    """
    SERVICE = "ContractAccrual"

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
        Retrieve all ContractAccruals

        Returns all ContractAccruals available to the Company, according to the parameters provided

        :calls: ``get /contractaccruals``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of ContractAccruals.
        :rtype: list
        """

        _, _, contract_accruals = self.http_client.get("/contractaccruals", params=params)
        return contract_accruals

    def retrieve(self, document_number):
        """
        Retrieve a single ContractAccruals

        Returns a single ContractAccruals according to the unique ContractAccruals ID provided
        If the specified ContractAccruals does not exist, this query returns an error

        :calls: ``get /contractaccruals/{document_number}``
        :param int id: Unique identifier of a ContractAccruals.
        :return: Dictionary that support attriubte-style access and represent ContractAccruals resource.
        :rtype: dict
        """
        _, _, contract_accrual = self.http_client.get(
            "/contractaccruals/{document_number}".format(document_number=document_number))
        return contract_accrual

    def create(self, *args, **kwargs):
        """
        Create a ContractAccruals

        Creates a new ContractAccruals
        **Notice** the ContractAccruals's name **must** be unique within the scope of the resource_type

        :calls: ``post /contractaccruals``
        :param tuple *args: (optional) Single object representing ContractAccruals resource.
        :param dict **kwargs: (optional) Customer attributes.
        :return: Dictionary that support attriubte-style access and represents newely created ContractAccruals resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for ContractAccruals are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, customer = self.http_client.post("/contractaccruals", body=attributes)
        return customer

    def update(self, document_number, *args, **kwargs):
        """
        Update a ContractAccruals

        Updates a ContractAccruals's information
        If the specified ContractAccruals does not exist, this query will return an error
        **Notice** if you want to update a ContractAccruals, you **must** make sure the ContractAccruals's name is unique within the scope of the specified resource

        :calls: ``put /contractaccruals/{document_number}``
        :param int id: Unique identifier of a ContractAccruals.
        :param tuple *args: (optional) Single object representing ContractAccruals resource which attributes should be updated.
        :param dict **kwargs: (optional) ContractAccruals attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated ContractAccruals resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for ContractAccruals are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, contract_accrual = self.http_client.put(
            "/contractaccruals/{document_number}".format(document_number=document_number), body=attributes)
        return contract_accrual

    def destroy(self, document_number):
        """
        Delete a ContractAccruals

        Deletes an existing ContractAccruals
        If the specified ContractAccruals is assigned to any resource, we will remove this ContractAccruals from all such resources
        If the specified ContractAccruals does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /contractaccruals/{document_number}``
        :param int id: Unique identifier of a ContractAccruals.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete(
            "/contractaccruals/{document_number}".format(document_number=document_number))
        return status_code == 204
