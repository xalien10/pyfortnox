class AbsenceTransactionsService(object):
    """
    :class:`fortnox.AbsenceTransactions` is used by :class:`fortnox.Client` to make
    actions related to Absence Transactions resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Absence Transactions to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['EmployeeId', 'CauseCode', 'Date', 'Extent']
    SERVICE = "AbsenceTransaction"

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
        Retrieve all AbsenceTransactions

        Returns all AbsenceTransactions available to the Company, according to the parameters provided

        :calls: ``get /absencetransactions``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of AbsenceTransactions.
        :rtype: list
        """

        _, _, absence_transactions = self.http_client.get("/absencetransactions", params=params)
        return absence_transactions

    def retrieve(self, employee_id, date, cause_code):
        """
        Retrieve a single AbsenceTransactions

        Returns a single AbsenceTransactions according to the unique AbsenceTransactions ID provided
        If the specified AbsenceTransactions does not exist, this query returns an error

        :calls: ``get /absencetransactions/{EmployeeId}/{Date}/{CauseCode}``
        :param int id: Unique identifier of a AbsenceTransactions.
        :return: Dictionary that support attriubte-style access and represent AbsenceTransactions resource.
        :rtype: dict
        """
        _, _, absence_transaction = self.http_client.get(
            "/absencetransactions/{EmployeeId}/{Date}/{CauseCode}".format(EmployeeId=employee_id, Date=date,
                                                                          CauseCode=cause_code))
        return absence_transaction

    def create(self, *args, **kwargs):
        """
        Create a AbsenceTransactions

        Creates a new AbsenceTransactions
        **Notice** the AbsenceTransaction's name **must** be unique within the scope of the resource_type

        :calls: ``post /absencetransactions``
        :param tuple *args: (optional) Single object representing AbsenceTransactions resource.
        :param dict **kwargs: (optional) AbsenceTransaction attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Customer resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for AbsenceTransaction are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, absence_transaction = self.http_client.post("/absencetransactions", body=attributes)
        return absence_transaction

    def update(self, employee_id, date, cause_code, *args, **kwargs):
        """
        Update a AbsenceTransaction

        Updates a AbsenceTransaction's information
        If the specified Absence Transaction does not exist, this query will return an error
        **Notice** if you want to update a Absence Transaction, you **must** make sure the AbsenceTransaction's name is unique within the scope of the specified resource

        :calls: ``put /absencetransactions/{EmployeeId}/{Date}/{CauseCode}``
        :param int id: Unique identifier of a AbsenceTransaction.
        :param tuple *args: (optional) Single object representing Absence Transaction resource which attributes should be updated.
        :param dict **kwargs: (optional) AbsenceTransaction attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated AbsenceTransactions resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for AbsenceTransaction are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, absence_transaction = self.http_client.put(
            "/absencetransactions/{EmployeeId}/{Date}/{CauseCode}".format(EmployeeId=employee_id, Date=date,
                                                                          CauseCode=cause_code), body=attributes)
        return absence_transaction

    def destroy(self, employee_id, date, cause_code):
        """
        Delete a AbsenceTransaction

        Deletes an existing AbsenceTransaction
        If the specified Absence Transaction is assigned to any resource, we will remove this Absence Transaction from all such resources
        If the specified Absence Transaction does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /absencetransactions/{EmployeeId}/{Date}/{CauseCode}``
        :param int id: Unique identifier of a AbsenceTransactions.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete(
            "/absencetransactions/{EmployeeId}/{Date}/{CauseCode}".format(EmployeeId=employee_id, Date=date,
                                                                          CauseCode=cause_code))
        return status_code == 204
