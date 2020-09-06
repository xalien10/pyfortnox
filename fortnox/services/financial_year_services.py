class FinancialYearService(object):
    """
    :class:`fortnox.FinancialYearService` is used by :class:`fortnox.Client` to make
    actions related to FinancialYear resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for FinancialYear to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['FromDate', 'ToDate', 'AccountChartType']
    SERVICE = "FinancialYear"

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
        Retrieve all FinancialYears

        Returns all FinancialYears available to the Company, according to the parameters provided

        :calls: ``get /financialyears``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of FinancialYears.
        :rtype: list
        """

        _, _, financial_years = self.http_client.get("/financialyears", params=params)
        return financial_years

    def retrieve(self, id):
        """
        Retrieve a single FinancialYear

        Returns a single FinancialYear according to the unique FinancialYear ID provided
        If the specified FinancialYear does not exist, this query returns an error

        :calls: ``get /financialyears/{id}``
        :param int id: Unique identifier of a FinancialYear.
        :return: Dictionary that support attriubte-style access and represent FinancialYear resource.
        :rtype: dict
        """
        _, _, financial_year = self.http_client.get("/financialyears/{id}".format(id=id))
        return financial_year

    def create(self, *args, **kwargs):
        """
        Create a FinancialYear

        Creates a new FinancialYear
        **Notice** the FinancialYear's name **must** be unique within the scope of the resource_type

        :calls: ``post /financialyears``
        :param tuple *args: (optional) Single object representing FinancialYear resource.
        :param dict **kwargs: (optional) FinancialYear attributes.
        :return: Dictionary that support attriubte-style access and represents newely created FinancialYear resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for FinancialYear are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, financial_year = self.http_client.post("/financialyears", body=attributes)
        return financial_year
