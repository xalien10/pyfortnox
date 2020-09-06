class InvoiceFileConnectionService(object):
    """
    :class:`fortnox.InvoiceFileConnectionService` is used by :class:`fortnox.Client` to make
    actions related to InvoiceFileConnection resource.

    Normally you won't instantiate this class directly.
    """
    # TODO: Need to implement carefully and exceptionally

    """
    Allowed attributes for InvoiceFileConnection to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Name']
    SERVICE = "InvoiceFileConnection"

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
        Retrieve all InvoiceFileConnection

        Returns all InvoiceFileConnection available to the Company, according to the parameters provided

        :calls: ``get /<specific-service-path>``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of InvoiceFileConnection.
        :rtype: list
        """

        _, _, customers = self.http_client.get("/<specific-service-path>", params=params)
        return customers

    def retrieve(self, id):
        """
        Retrieve a single InvoiceFileConnection

        Returns a single InvoiceFileConnection according to the unique InvoiceFileConnection ID provided
        If the specified InvoiceFileConnection does not exist, this query returns an error

        :calls: ``get /<specific-service-path>/{id}``
        :param int id: Unique identifier of a InvoiceFileConnection.
        :return: Dictionary that support attriubte-style access and represent InvoiceFileConnection resource.
        :rtype: dict
        """
        _, _, customer = self.http_client.get("/<specific-service-path>/{id}".format(id=id))
        return customer

    def create(self, *args, **kwargs):
        """
        Create a InvoiceFileConnection

        Creates a new InvoiceFileConnection
        **Notice** the InvoiceFileConnection's name **must** be unique within the scope of the resource_type

        :calls: ``post /<specific-service-path>``
        :param tuple *args: (optional) Single object representing InvoiceFileConnection resource.
        :param dict **kwargs: (optional) Customer attributes.
        :return: Dictionary that support attriubte-style access and represents newely created InvoiceFileConnection resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for InvoiceFileConnection are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, customer = self.http_client.post("/<specific-service-path>", body=attributes)
        return customer

    def update(self, id, *args, **kwargs):
        """
        Update a InvoiceFileConnection

        Updates a InvoiceFileConnection's information
        If the specified InvoiceFileConnection does not exist, this query will return an error
        **Notice** if you want to update a InvoiceFileConnection, you **must** make sure the InvoiceFileConnection's name is unique within the scope of the specified resource

        :calls: ``put /<specific-service-path>/{id}``
        :param int id: Unique identifier of a InvoiceFileConnection.
        :param tuple *args: (optional) Single object representing InvoiceFileConnection resource which attributes should be updated.
        :param dict **kwargs: (optional) InvoiceFileConnection attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated InvoiceFileConnection resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for InvoiceFileConnection are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, customer = self.http_client.put("/<specific-service-path>/{id}".format(id=id), body=attributes)
        return customer

    def destroy(self, id):
        """
        Delete a InvoiceFileConnection

        Deletes an existing InvoiceFileConnection
        If the specified InvoiceFileConnection is assigned to any resource, we will remove this InvoiceFileConnection from all such resources
        If the specified InvoiceFileConnection does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /<specific-service-path>/{id}``
        :param int id: Unique identifier of a InvoiceFileConnection.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/<specific-service-path>/{id}".format(id=id))
        return status_code == 204
