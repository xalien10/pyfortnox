class PredefinedVoucherSeriesService(object):
    """
    :class:`fortnox.PredefinedVoucherSeriesService` is used by :class:`fortnox.Client` to make
    actions related to Predefined Voucher Series resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Predefined Voucher Series to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = []
    SERVICE = "PreDefinedVoucherSeries"

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
        Retrieve all PreDefined Vouchers

        Returns all Predefined Vouchers Series available to the Company, according to the parameters provided

        :calls: ``get /predefinedvoucherseries``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of PreDefined Voucher Series.
        :rtype: list
        """

        _, _, predefined_voucher_series_collection = self.http_client.get("/predefinedvoucherseries", params=params)
        return predefined_voucher_series_collection

    def retrieve(self, name):
        """
        Retrieve a single PreDefined Voucher Series

        Returns a single PreDefined Voucher Series according to the unique PreDefined Voucher Series ID provided
        If the specified PreDefined Voucher Series does not exist, this query returns an error

        :calls: ``get /predefinedvoucherseries/{name}``
        :param int id: Unique identifier of a PreDefined Voucher Series.
        :return: Dictionary that support attriubte-style access and represent PreDefined Voucher Series resource.
        :rtype: dict
        """
        _, _, predefined_voucher_series = self.http_client.get("/predefinedvoucherseries/{name}".format(name=name))
        return predefined_voucher_series

    def update(self, name, *args, **kwargs):
        """
        Update a PreDefined Voucher Series

        Updates a PreDefined Voucher's information
        If the specified PreDefined Voucher does not exist, this query will return an error
        **Notice** if you want to update a PreDefined Voucher, you **must** make sure the PreDefined Voucher's name is unique within the scope of the specified resource

        :calls: ``put /predefinedvoucherseries/{name}``
        :param int id: Unique identifier of a PreDefined Voucher.
        :param tuple *args: (optional) Single object representing PreDefined Voucher resource which attributes should be updated.
        :param dict **kwargs: (optional) PreDefined Voucher attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated PreDefined Voucher resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for PreDefined Voucher are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, predefined_voucher_series = self.http_client.put("/predefinedvoucherseries/{name}".format(name=name),
                                                               body=attributes)
        return predefined_voucher_series
