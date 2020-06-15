class VoucherService(object):
    """
    :class:`fortnox.VoucherService` is used by :class:`fortnox.Client` to make
    actions related to Voucher resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Voucher to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Description', 'VoucherSeries', 'TransactionDate', 'VoucherRows']

    """
    VoucherRows has the following structures:
        "VoucherRows": [
            {
                "Description": "Företagskonto / checkkonto / affärskonto",
                "Debit": "1500",
                "Account": "1930",
                "Credit": "0"
            },
            {
                "Description": "Kassa",
                "Debit": "0",
                "Account": "1910",
                "Credit": "1500"
            },
            .................
        ]
    """

    SERVICE = "Voucher"

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
        Retrieve all Voucher

        Returns all Voucher available to the Company, according to the parameters provided

        :calls: ``get /vouchers``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Voucher.
        :rtype: list
        """

        _, _, vouchers = self.http_client.get("/vouchers", params=params)
        return vouchers

    def retrieve_sublist(self, voucher_series):
        """
        Retrieve a sublist Voucher from a series

        Returns a single Voucher according to the unique Voucher ID provided
        If the specified Voucher does not exist, this query returns an error

        :calls: ``get /vouchers/sublist/{voucher_series}``
        :param int id: Unique identifier of a Voucher.
        :return: Dictionary that support attriubte-style access and represent Voucher resource.
        :rtype: dict
        """
        _, _, vouchers = self.http_client.get(
            "/vouchers/sublist/{voucher_series}".format(voucher_series=voucher_series))
        return vouchers

    def retrieve(self, voucher_series, id):
        """
        Retrieve a single Voucher

        Returns a single Voucher according to the unique Voucher ID provided
        If the specified Voucher does not exist, this query returns an error

        :calls: ``get /vouchers/sublist/{voucher_series}/{id}``
        :param int id: Unique identifier of a Voucher.
        :return: Dictionary that support attriubte-style access and represent Voucher resource.
        :rtype: dict
        """
        _, _, voucher = self.http_client.get(
            "/vouchers/sublist/{voucher_series}/{id}".format(voucher_series=voucher_series, id=id))
        return voucher

    def create(self, *args, **kwargs):
        """
        Create a Voucher

        Creates a new Voucher
        **Notice** the Voucher's name **must** be unique within the scope of the resource_type

        :calls: ``post /vouchers``
        :param tuple *args: (optional) Single object representing Voucher resource.
        :param dict **kwargs: (optional) voucher attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Voucher resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Voucher are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, voucher = self.http_client.post("/vouchers", body=attributes)
        return voucher
