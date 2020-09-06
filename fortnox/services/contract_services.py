class ContractService(object):
    """
    :class:`fortnox.ContractService` is used by :class:`fortnox.Client` to make
    actions related to Contracts resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Contracts to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['CustomerNumber', 'InvoiceRows', 'PeriodStart', 'PeriodEnd']

    """
    InvoiceRows will have the following structures:
        "InvoiceRows": [
          {
            "ArticleNumber": "11",
            "DeliveredQuantity": 1000
          },
          {
            "ArticleNumber": "13",
            "DeliveredQuantity": 100
          },
          .............
        ]
    """
    SERVICE = "Contract"

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
        Retrieve all Contracts

        Returns all Contracts available to the Company, according to the parameters provided

        :calls: ``get /contracts``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Contracts.
        :rtype: list
        """

        _, _, contracts = self.http_client.get("/contracts", params=params)
        return contracts

    def retrieve(self, document_number):
        """
        Retrieve a single Contracts

        Returns a single Contracts according to the unique Contracts ID provided
        If the specified Contracts does not exist, this query returns an error

        :calls: ``get /contracts/{document_number}``
        :param int id: Unique identifier of a Contracts.
        :return: Dictionary that support attriubte-style access and represent Contracts resource.
        :rtype: dict
        """
        _, _, contract = self.http_client.get("/contracts/{document_number}".format(document_number=document_number))
        return contract

    def create(self, *args, **kwargs):
        """
        Create a Contracts

        Creates a new Contracts
        **Notice** the Contracts's name **must** be unique within the scope of the resource_type

        :calls: ``post /contracts``
        :param tuple *args: (optional) Single object representing Contracts resource.
        :param dict **kwargs: (optional) Customer attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Contracts resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Contracts are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, contract = self.http_client.post("/contracts", body=attributes)
        return contract

    def update(self, document_number, *args, **kwargs):
        """
        Update a Contracts

        Updates a Contracts's information
        If the specified Contracts does not exist, this query will return an error
        **Notice** if you want to update a Contracts, you **must** make sure the Contracts's name is unique within the scope of the specified resource

        :calls: ``put /contracts/{document_number}``
        :param int id: Unique identifier of a Contracts.
        :param tuple *args: (optional) Single object representing Contracts resource which attributes should be updated.
        :param dict **kwargs: (optional) Contracts attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Contracts resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Contracts are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, contract = self.http_client.put("/contracts/{document_number}".format(document_number=document_number),
                                              body=attributes)
        return contract
