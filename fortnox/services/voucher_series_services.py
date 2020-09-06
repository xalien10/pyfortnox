class VoucherSeriesService(object):
    """
    :class:`fortnox.VoucherSeriesService` is used by :class:`fortnox.Client` to make
    actions related to VoucherSeries resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for VoucherSeries to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Code', 'Description']
    SERVICE = "VoucherSeries"

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
        Retrieve all VoucherSeries

        Returns all VoucherSeries available to the Company, according to the parameters provided

        :calls: ``get /voucherseries``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of VoucherSeries.
        :rtype: list
        """

        _, _, voucher_series_collection = self.http_client.get("/voucherseries", params=params)
        return voucher_series_collection

    def retrieve(self, code):
        """
        Retrieve a single VoucherSeries

        Returns a single VoucherSeries according to the unique VoucherSeries ID provided
        If the specified VoucherSeries does not exist, this query returns an error

        :calls: ``get /voucherseries/{code}``
        :param int id: Unique identifier of a VoucherSeries.
        :return: Dictionary that support attriubte-style access and represent VoucherSeries resource.
        :rtype: dict
        """
        _, _, voucher_series = self.http_client.get("/voucherseries/{code}".format(code=code))
        return voucher_series

    def create(self, *args, **kwargs):
        """
        Create a VoucherSeries

        Creates a new VoucherSeries
        **Notice** the VoucherSeries's name **must** be unique within the scope of the resource_type

        :calls: ``post /voucherseries``
        :param tuple *args: (optional) Single object representing VoucherSeries resource.
        :param dict **kwargs: (optional) voucher_series attributes.
        :return: Dictionary that support attriubte-style access and represents newely created VoucherSeries resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for VoucherSeries are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, voucher_series = self.http_client.post("/voucherseries", body=attributes)
        return voucher_series

    def update(self, code, *args, **kwargs):
        """
        Update a VoucherSeries

        Updates a VoucherSeries's information
        If the specified VoucherSeries does not exist, this query will return an error
        **Notice** if you want to update a VoucherSeries, you **must** make sure the VoucherSeries's name is unique within the scope of the specified resource

        :calls: ``put /voucherseries/{code}``
        :param int id: Unique identifier of a VoucherSeries.
        :param tuple *args: (optional) Single object representing VoucherSeries resource which attributes should be updated.
        :param dict **kwargs: (optional) VoucherSeries attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated VoucherSeries resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for VoucherSeries are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, voucher_series = self.http_client.put("/voucherseries/{code}".format(code=code), body=attributes)
        return voucher_series
