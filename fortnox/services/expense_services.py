class ExpenseService(object):
    """
    :class:`fortnox.ExpenseService` is used by :class:`fortnox.Client` to make
    actions related to Expense resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Expense to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Code', 'Text', 'Account']
    SERVICE = "Expense"

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
        Retrieve all Expenses

        Returns all Expenses available to the Company, according to the parameters provided

        :calls: ``get /expenses``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Expenses.
        :rtype: list
        """

        _, _, expenses = self.http_client.get("/expenses", params=params)
        return expenses

    def retrieve(self, expense_code):
        """
        Retrieve a single Expense

        Returns a single Expense according to the unique Expense ID provided
        If the specified Expense does not exist, this query returns an error

        :calls: ``get /expenses/{expense_code}``
        :param int id: Unique identifier of an Expense.
        :return: Dictionary that support attriubte-style access and represent Expense resource.
        :rtype: dict
        """
        _, _, expense = self.http_client.get("/expenses/{expense_code}".format(expense_code=expense_code))
        return expense

    def create(self, *args, **kwargs):
        """
        Create an Expense

        Creates a new Expense
        **Notice** the Expense's name **must** be unique within the scope of the resource_type

        :calls: ``post /expenses``
        :param tuple *args: (optional) Single object representing Expense resource.
        :param dict **kwargs: (optional) Expenses attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Expense resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Expense are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, expense = self.http_client.post("/expenses", body=attributes)
        return expense
