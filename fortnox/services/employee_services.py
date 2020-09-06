class EmployeeService(object):
    """
    :class:`fortnox.EmployeeService` is used by :class:`fortnox.Client` to make
    actions related to Employee resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Employee to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['EmployeeId', 'FirstName', 'LastName']
    SERVICE = "Employee"

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
        Retrieve all Employees

        Returns all Employees available to the Company, according to the parameters provided

        :calls: ``get /employees``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Employees.
        :rtype: list
        """

        _, _, employees = self.http_client.get("/employees", params=params)
        return employees

    def create(self, *args, **kwargs):
        """
        Create a Employee

        Creates a new Employee
        **Notice** the Employee's name **must** be unique within the scope of the resource_type

        :calls: ``post /customers``
        :param tuple *args: (optional) Single object representing Employee resource.
        :param dict **kwargs: (optional) Employee attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Employee resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Employee are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, employee = self.http_client.post("/employees", body=attributes)
        return employee

    def retrieve(self, id):
        """
        Retrieve a single Employee

        Returns a single Employee according to the unique Employee ID provided
        If the specified Employee does not exist, this query returns an error

        :calls: ``get /employees/{id}``
        :param int id: Unique identifier of a employee.
        :return: Dictionary that support attriubte-style access and represent employee resource.
        :rtype: dict
        """
        _, _, employee = self.http_client.get("/employees/{id}".format(id=id))
        return employee

    def update(self, id, *args, **kwargs):
        """
        Update an Employee

        Updates an Employee's information
        If the specified Employee does not exist, this query will return an error
        **Notice** if you want to update an Employee, you **must** make sure the Employee's name is unique within the scope of the specified resource

        :calls: ``put /employees/{id}``
        :param int id: Unique identifier of a employee.
        :param tuple *args: (optional) Single object representing employee resource which attributes should be updated.
        :param dict **kwargs: (optional) employee attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated employee resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Employee are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, employee = self.http_client.put("/employees/{id}".format(id=id), body=attributes)
        return employee
