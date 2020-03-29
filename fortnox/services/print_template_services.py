class PrintTemplateService(object):
    """
    :class:`fortnox.PrintTemplateService` is used by :class:`fortnox.Client` to make
    actions related to PrintTemplate resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for PrintTemplate to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = []
    SERVICE = "PrintTemplate"

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
        Retrieve all PrintTemplate

        Returns all PrintTemplate available to the Company, according to the parameters provided

        :calls: ``get /printtemplates``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of PrintTemplate.
        :rtype: list
        """

        _, _, print_templates = self.http_client.get("/printtemplates", params=params)
        return print_templates
