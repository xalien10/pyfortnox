class PredefinedAccountService(object):
    """
    :class:`fortnox.PredefinedAccountService` is used by :class:`fortnox.Client` to make
    actions related to Predefined Account resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for PredefinedAccount to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = []
    SERVICE = "PreDefinedAccount"

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
        Retrieve all Predefined Accounts

        Returns all Predefined Accounts available to the Company, according to the parameters provided

        :calls: ``get /predefinedaccounts``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Predefined Accounts.
        :rtype: list
        """

        _, _, predefined_accounts = self.http_client.get("/predefinedaccounts", params=params)
        return predefined_accounts

    def retrieve(self, name):
        """
        Retrieve a single Predefined Account

        Returns a single Predefined Account according to the unique Predefined Account ID provided
        If the specified Predefined Account does not exist, this query returns an error

        :calls: ``get /predefinedaccounts/{name}``
        :param int id: Unique identifier of a Predefined Account.
        :return: Dictionary that support attriubte-style access and represent Predefined Account resource.
        :rtype: dict
        """
        _, _, predefined_account = self.http_client.get("/predefinedaccounts/{name}".format(name=name))
        return predefined_account

    def update(self, name, *args, **kwargs):
        """
        Update a Predefined Account

        Updates a Predefined Account's information
        If the specified Predefined Account does not exist, this query will return an error
        **Notice** if you want to update a Predefined Account, you **must** make sure the Predefined Account's name is unique within the scope of the specified resource

        :calls: ``put /predefinedaccounts/{name}``
        :param int id: Unique identifier of a Predefined Account.
        :param tuple *args: (optional) Single object representing Predefined Account resource which attributes should be updated.
        :param dict **kwargs: (optional) Predefined Account attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Predefined Account resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for PredefinedAccount are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, predefined_account = self.http_client.put("/predefinedaccounts/{name}".format(name=name), body=attributes)
        return predefined_account
