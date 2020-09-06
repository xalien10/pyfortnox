class TrustedDomainService(object):
    """
    :class:`fortnox.TrustedDomainService` is used by :class:`fortnox.Client` to make
    actions related to TrustedDomain resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for TrustedDomain to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Domain']
    SERVICE = "TrustedDomain"

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
        Retrieve all TrustedDomain

        Returns all TrustedDomain available to the Company, according to the parameters provided

        :calls: ``get /emailtrusteddomains``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of TrustedDomain.
        :rtype: list
        """

        _, _, email_trusted_domains = self.http_client.get("/emailtrusteddomains", params=params)
        return email_trusted_domains

    def retrieve(self, id):
        """
        Retrieve a single TrustedDomain

        Returns a single TrustedDomain according to the unique TrustedDomain ID provided
        If the specified TrustedDomain does not exist, this query returns an error

        :calls: ``get /emailtrusteddomains/{id}``
        :param int id: Unique identifier of a TrustedDomain.
        :return: Dictionary that support attriubte-style access and represent TrustedDomain resource.
        :rtype: dict
        """
        _, _, email_trusted_domain = self.http_client.get("/emailtrusteddomains/{id}".format(id=id))
        return email_trusted_domain

    def create(self, *args, **kwargs):
        """
        Create a TrustedDomain

        Creates a new TrustedDomain
        **Notice** the TrustedDomain's name **must** be unique within the scope of the resource_type

        :calls: ``post /emailtrusteddomains``
        :param tuple *args: (optional) Single object representing TrustedDomain resource.
        :param dict **kwargs: (optional) email_trusted_domain attributes.
        :return: Dictionary that support attriubte-style access and represents newely created TrustedDomain resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for TrustedDomain are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, email_trusted_domain = self.http_client.post("/emailtrusteddomains", body=attributes)
        return email_trusted_domain

    def destroy(self, id):
        """
        Delete a TrustedDomain

        Deletes an existing TrustedDomain
        If the specified TrustedDomain is assigned to any resource, we will remove this TrustedDomain from all such resources
        If the specified TrustedDomain does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /emailtrusteddomains/{id}``
        :param int id: Unique identifier of a TrustedDomain.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/emailtrusteddomains/{id}".format(id=id))
        return status_code == 204
