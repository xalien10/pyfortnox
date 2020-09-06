class TrustedSenderService(object):
    """
    :class:`fortnox.TrustedSenderService` is used by :class:`fortnox.Client` to make
    actions related to TrustedSender resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for TrustedSender to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Email']
    SERVICE = "TrustedSender"

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
        Retrieve all TrustedSender

        Returns all TrustedSender available to the Company, according to the parameters provided

        :calls: ``get /emailsenders``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of TrustedSender.
        :rtype: list
        """

        _, _, email_senders = self.http_client.get("/emailsenders", params=params)
        return email_senders

    def retrieve(self, id):
        """
        Retrieve a single TrustedSender

        Returns a single TrustedSender according to the unique TrustedSender ID provided
        If the specified TrustedSender does not exist, this query returns an error

        :calls: ``get /emailsenders/trusted/{id}``
        :param int id: Unique identifier of a TrustedSender.
        :return: Dictionary that support attriubte-style access and represent TrustedSender resource.
        :rtype: dict
        """
        _, _, email_sender = self.http_client.get("/emailsenders/trusted/{id}".format(id=id))
        return email_sender

    def create(self, *args, **kwargs):
        """
        Create a TrustedSender

        Creates a new TrustedSender
        **Notice** the TrustedSender's name **must** be unique within the scope of the resource_type

        :calls: ``post /emailsenders/trusted/``
        :param tuple *args: (optional) Single object representing TrustedSender resource.
        :param dict **kwargs: (optional) email_sender attributes.
        :return: Dictionary that support attriubte-style access and represents newely created TrustedSender resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for TrustedSender are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, email_sender = self.http_client.post("/emailsenders/trusted/", body=attributes)
        return email_sender

    def destroy(self, id):
        """
        Delete a TrustedSender

        Deletes an existing TrustedSender
        If the specified TrustedSender is assigned to any resource, we will remove this TrustedSender from all such resources
        If the specified TrustedSender does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /emailsenders/trusted/{id}``
        :param int id: Unique identifier of a TrustedSender.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/emailsenders/trusted/{id}".format(id=id))
        return status_code == 204
