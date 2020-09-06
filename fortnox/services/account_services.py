class AccountsService(object):
    """
    :class:`fortnox.AccountsService` is used by :class:`fortnox.Client` to make
    actions related to <specific-service> resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Accounts to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Number', 'Description']
    SERVICE = "Account"

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
        Retrieve all Accounts

        Returns all Accounts available to the Company, according to the parameters provided

        :calls: ``get /accounts``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Customers.
        :rtype: list
        """

        _, _, accounts = self.http_client.get("/accounts", params=params)
        return accounts

    def retrieve(self, id):
        """
        Retrieve a single Accounts

        Returns a single Account according to the unique Account ID provided
        If the specified Account does not exist, this query returns an error

        :calls: ``get /accounts/{id}``
        :param int id: Unique identifier of a Account.
        :return: Dictionary that support attriubte-style access and represent Accounts resource.
        :rtype: dict
        """
        _, _, account = self.http_client.get("/accounts/{id}".format(id=id))
        return account

    def create(self, *args, **kwargs):
        """
        Create a Account

        Creates a new Accounts
        **Notice** the Account's name **must** be unique within the scope of the resource_type

        :calls: ``post /accounts``
        :param tuple *args: (optional) Single object representing Account resource.
        :param dict **kwargs: (optional) Account attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Account resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Account are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, account = self.http_client.post("/accounts", body=attributes)
        return account

    def update(self, id, *args, **kwargs):
        """
        Update a Account

        Updates a Account's information
        If the specified Account does not exist, this query will return an error
        **Notice** if you want to update a Account, you **must** make sure the Account's name is unique within the scope of the specified resource

        :calls: ``put /accounts/{id}``
        :param int id: Unique identifier of a Account.
        :param tuple *args: (optional) Single object representing Accounts resource which attributes should be updated.
        :param dict **kwargs: (optional) account attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Accounts resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Account are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, account = self.http_client.put("/accounts/{id}".format(id=id), body=attributes)
        return account
