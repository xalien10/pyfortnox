class AttendanceTransactionsService(object):
    """
    :class:`fortnox.AttendanceTransactionsService` is used by :class:`fortnox.Client` to make
    actions related to Attendance Transactions resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Attendance Transactions to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['EmployeeId', 'CauseCode', 'Date', 'Hours']
    SERVICE = "AttendanceTransaction"

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
        Retrieve all AttendanceTransactions

        Returns all AttendanceTransaction available to the Company, according to the parameters provided

        :calls: ``get /attendancetransactions``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of AttendanceTransactions.
        :rtype: list
        """

        _, _, attendance_transactions = self.http_client.get("/attendancetransactions", params=params)
        return attendance_transactions

    def retrieve(self, employee_id, date, cause_code):
        """
        Retrieve a single Attendance Transaction

        Returns a single Attendance Transaction according to the unique Attendance Transaction ID provided
        If the specified Attendance Transaction does not exist, this query returns an error

        :calls: ``get /attendancetransactions/{employee_id}/{date}/{cause_code}``
        :param int id: Unique identifier of an Attendance Transaction.
        :return: Dictionary that support attriubte-style access and represent Attendance Transaction resource.
        :rtype: dict
        """
        _, _, attendance_transaction = self.http_client.get(
            "/attendancetransactions/{employee_id}/{date}/{cause_code}".format(employee_id=employee_id, date=date,
                                                                               cause_code=cause_code))
        return attendance_transaction

    def create(self, *args, **kwargs):
        """
        Create an Attendance Transaction

        Creates a new Attendance Transaction
        **Notice** the Attendance Transaction's name **must** be unique within the scope of the resource_type

        :calls: ``post /attendancetransactions``
        :param tuple *args: (optional) Single object representing AttendanceTransaction resource.
        :param dict **kwargs: (optional) Attendance Transaction attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Attendance Transaction resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for AttendanceTransaction are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, attendance_transaction = self.http_client.post("/attendancetransactions", body=attributes)
        return attendance_transaction

    def update(self, employee_id, date, cause_code, *args, **kwargs):
        """
        Update an AttendanceTransaction

        Updates an AttendanceTransaction's information
        If the specified AttendanceTransaction does not exist, this query will return an error
        **Notice** if you want to update an AttendanceTransaction, you **must** make sure the AttendanceTransaction's name is unique within the scope of the specified resource

        :calls: ``put /attendancetransactions/{employee_id}/{date}/{cause_code}``
        :param int id: Unique identifier of an AttendanceTransaction.
        :param tuple *args: (optional) Single object representing AttendanceTransaction resource which attributes should be updated.
        :param dict **kwargs: (optional) AttendanceTransaction attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated AttendanceTransaction resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for AttendanceTransaction are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, attendance_transaction = self.http_client.put(
            "/attendancetransactions/{employee_id}/{date}/{cause_code}".format(employee_id=employee_id, date=date,
                                                                               cause_code=cause_code), body=attributes)
        return attendance_transaction

    def destroy(self, employee_id, date, cause_code):
        """
        Delete an AttendanceTransaction

        Deletes an existing AttendanceTransaction
        If the specified AttendanceTransaction is assigned to any resource, we will remove this AttendanceTransaction from all such resources
        If the specified AttendanceTransaction does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /attendancetransactions/{employee_id}/{date}/{cause_code}``
        :param int id: Unique identifier of an AttendanceTransaction.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete(
            "/attendancetransactions/{employee_id}/{date}/{cause_code}".format(employee_id=employee_id, date=date,
                                                                               cause_code=cause_code))
        return status_code == 204
