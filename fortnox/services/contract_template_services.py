class ContractTemplateService(object):
    """
    :class:`fortnox.ContractTemplateService` is used by :class:`fortnox.Client` to make
    actions related to ContractTemplate resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for ContractTemplate to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['ContractLength', 'Continuous', 'InvoiceInterval', 'InvoiceRows', 'TemplateName']

    """
    InvoiceRows should have the following structures,
        "InvoiceRows": [
          {
            "ArticleNumber": "11",
            "DeliveredQuantity": 10
          },
          {
            "ArticleNumber": "12",
            "DeliveredQuantity": 12
          },
          ....................
        ]
    """
    SERVICE = "ContractTemplate"

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
        Retrieve all ContractTemplate

        Returns all ContractTemplate available to the Company, according to the parameters provided

        :calls: ``get /contracttemplates``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of ContractTemplate.
        :rtype: list
        """

        _, _, contract_templates = self.http_client.get("/contracttemplates", params=params)
        return contract_templates

    def retrieve(self, template_number):
        """
        Retrieve a single ContractTemplate

        Returns a single ContractTemplate according to the unique ContractTemplate ID provided
        If the specified ContractTemplate does not exist, this query returns an error

        :calls: ``get /contracttemplates/{template_number}``
        :param int id: Unique identifier of a ContractTemplate.
        :return: Dictionary that support attriubte-style access and represent ContractTemplate resource.
        :rtype: dict
        """
        _, _, contract_template = self.http_client.get(
            "/contracttemplates/{template_number}".format(template_number=template_number))
        return contract_template

    def create(self, *args, **kwargs):
        """
        Create a ContractTemplate

        Creates a new ContractTemplate
        **Notice** the ContractTemplate's name **must** be unique within the scope of the resource_type

        :calls: ``post /contracttemplates``
        :param tuple *args: (optional) Single object representing ContractTemplate resource.
        :param dict **kwargs: (optional) contract_template attributes.
        :return: Dictionary that support attriubte-style access and represents newely created ContractTemplate resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for ContractTemplate are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, contract_template = self.http_client.post("/contracttemplates", body=attributes)
        return contract_template

    def update(self, template_number, *args, **kwargs):
        """
        Update a ContractTemplate

        Updates a ContractTemplate's information
        If the specified ContractTemplate does not exist, this query will return an error
        **Notice** if you want to update a ContractTemplate, you **must** make sure the ContractTemplate's name is unique within the scope of the specified resource

        :calls: ``put /contracttemplates/{template_number}``
        :param int id: Unique identifier of a ContractTemplate.
        :param tuple *args: (optional) Single object representing ContractTemplate resource which attributes should be updated.
        :param dict **kwargs: (optional) ContractTemplate attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated ContractTemplate resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for ContractTemplate are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, contract_template = self.http_client.put(
            "/contracttemplates/{template_number}".format(template_number=template_number), body=attributes)
        return contract_template
