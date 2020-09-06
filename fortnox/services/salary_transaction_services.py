class SalaryTransactionService(object):
    """
    :class:`fortnox.SalaryTransactionService` is used by :class:`fortnox.Client` to make
    actions related to SalaryTransaction resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for SalaryTransaction to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['EmployeeId', 'SalaryCode', 'Date', 'Number', 'Amount']
    SERVICE = "SalaryTransaction"

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
        Retrieve all SalaryTransaction

        Returns all SalaryTransaction available to the Company, according to the parameters provided

        :calls: ``get /salarytransactions``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of SalaryTransaction.
        :rtype: list
        """

        _, _, salary_transactions = self.http_client.get("/salarytransactions", params=params)
        return salary_transactions

    def retrieve(self, salary_row):
        """
        Retrieve a single SalaryTransaction

        Returns a single SalaryTransaction according to the unique SalaryTransaction ID provided
        If the specified SalaryTransaction does not exist, this query returns an error

        :calls: ``get /salarytransactions/{salary_row}``
        :param int id: Unique identifier of a SalaryTransaction.
        :return: Dictionary that support attriubte-style access and represent SalaryTransaction resource.
        :rtype: dict
        """
        _, _, salary_transaction = self.http_client.get(
            "/salarytransactions/{salary_row}".format(salary_row=salary_row))
        return salary_transaction

    def create(self, *args, **kwargs):
        """
        Create a SalaryTransaction

        Creates a new SalaryTransaction
        **Notice** the SalaryTransaction's name **must** be unique within the scope of the resource_type

        :calls: ``post /salarytransactions``
        :param tuple *args: (optional) Single object representing SalaryTransaction resource.
        :param dict **kwargs: (optional) salary_transaction attributes.
        :return: Dictionary that support attriubte-style access and represents newely created SalaryTransaction resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for SalaryTransaction are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, salary_transaction = self.http_client.post("/salarytransactions", body=attributes)
        return salary_transaction

    def update(self, salary_row, *args, **kwargs):
        """
        Update a SalaryTransaction

        Updates a SalaryTransaction's information
        If the specified SalaryTransaction does not exist, this query will return an error
        **Notice** if you want to update a SalaryTransaction, you **must** make sure the SalaryTransaction's name is unique within the scope of the specified resource

        :calls: ``put /salarytransactions/{salary_row}``
        :param int id: Unique identifier of a SalaryTransaction.
        :param tuple *args: (optional) Single object representing SalaryTransaction resource which attributes should be updated.
        :param dict **kwargs: (optional) SalaryTransaction attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated SalaryTransaction resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for SalaryTransaction are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, salary_transaction = self.http_client.put(
            "/salarytransactions/{salary_row}".format(salary_row=salary_row), body=attributes)
        return salary_transaction

    def destroy(self, salary_row):
        """
        Delete a SalaryTransaction

        Deletes an existing SalaryTransaction
        If the specified SalaryTransaction is assigned to any resource, we will remove this SalaryTransaction from all such resources
        If the specified SalaryTransaction does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /salarytransactions/{salary_row}``
        :param int id: Unique identifier of a SalaryTransaction.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/salarytransactions/{salary_row}".format(salary_row=salary_row))
        return status_code == 204
