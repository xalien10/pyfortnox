class InboxService(object):
    """
    :class:`fortnox.InboxService` is used by :class:`fortnox.Client` to make
    actions related to Inbox resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Inbox to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['file', 'path']
    SERVICE = "Folders"

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
        Retrieve all Inbox

        Returns all Inbox available to the Company, according to the parameters provided

        :calls: ``get /inbox``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Inbox.
        :rtype: list
        """

        _, _, folders = self.http_client.get("/inbox", params=params)
        return folders

    def asset_register_list(self, **params):
        """
        Retrieve all Inbox

        Returns all Inbox available to the Company, according to the parameters provided

        :calls: ``get /inbox``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Inbox.
        :rtype: list
        """
        _, _, folders = self.http_client.get("/inbox/inbox_a", params=params)
        return folders

    def daily_takings_list(self, **params):
        """
        Retrieve all Inbox

        Returns all Inbox available to the Company, according to the parameters provided

        :calls: ``get /inbox``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Inbox.
        :rtype: list
        """
        _, _, folders = self.http_client.get("/inbox/inbox_d", params=params)
        return folders

    def supplier_invoices_list(self, **params):
        """
        Retrieve all Inbox

        Returns all Inbox available to the Company, according to the parameters provided

        :calls: ``get /inbox``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Inbox.
        :rtype: list
        """
        _, _, folders = self.http_client.get("/inbox/inbox_s", params=params)
        return folders

    def vouchers_list(self, **params):
        """
        Retrieve all Inbox

        Returns all Inbox available to the Company, according to the parameters provided

        :calls: ``get /inbox``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Inbox.
        :rtype: list
        """
        _, _, folders = self.http_client.get("/inbox/inbox_v", params=params)
        return folders

    def bank_files_list(self, **params):
        """
        Retrieve all Inbox

        Returns all Inbox available to the Company, according to the parameters provided

        :calls: ``get /inbox``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Inbox.
        :rtype: list
        """
        _, _, folders = self.http_client.get("/inbox/inbox_b", params=params)
        return folders

    def payroll_files_list(self, **params):
        """
        Retrieve all Inbox

        Returns all Inbox available to the Company, according to the parameters provided

        :calls: ``get /inbox``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Inbox.
        :rtype: list
        """
        _, _, folders = self.http_client.get("/inbox/inbox_l", params=params)
        return folders

    def customer_invoices_list(self, **params):
        """
        Retrieve all Inbox

        Returns all Inbox available to the Company, according to the parameters provided

        :calls: ``get /inbox``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Inbox.
        :rtype: list
        """
        _, _, folders = self.http_client.get("/inbox/inbox_kf", params=params)
        return folders

    def orders_list(self, **params):
        """
        Retrieve all Inbox

        Returns all Inbox available to the Company, according to the parameters provided

        :calls: ``get /inbox``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Inbox.
        :rtype: list
        """
        _, _, folders = self.http_client.get("/inbox/inbox_o", params=params)
        return folders

    def offers_list(self, **params):
        """
        Retrieve all Inbox

        Returns all Inbox available to the Company, according to the parameters provided

        :calls: ``get /inbox``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Inbox.
        :rtype: list
        """
        _, _, folders = self.http_client.get("/inbox/inbox_of", params=params)
        return folders

    def retrieve(self, file_id):
        """
        Retrieve a single file

        Returns a single Inbox according to the unique Inbox ID provided
        If the specified Inbox does not exist, this query returns an error

        :calls: ``get /inbox/{file_id}``
        :param int id: Unique identifier of a file.
        :return: Dictionary that support attriubte-style access and represent Inbox resource.
        :rtype: dict
        """
        _, _, folder = self.http_client.get("/inbox/{file_id}".format(file_id=file_id))
        return folder

    def create(self, *args, **kwargs):
        """
        Create a Inbox

        Creates a new Inbox
        **Notice** the Inbox's name **must** be unique within the scope of the resource_type

        :calls: ``post /inbox``
        :param tuple *args: (optional) Single object representing Inbox resource.
        :param dict **kwargs: (optional) folder attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Inbox resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Inbox files are missing')

        path_name = "/inbox"
        attributes = args[0] if args else kwargs
        # attributes = dict((k, v) for k, v in attributes.items() if k in self.OPTS_KEYS_TO_PERSIST)
        attributes.update({'service': self.SERVICE})

        # if folder path is specified
        path = attributes.get('path', None)
        if path:
            path_name = "/inbox?path={path}".format(path=path)

        # get the buffered file
        file = attributes.get('file', None)
        file_name = attributes.pop('file_name', None)
        for k in self.OPTS_KEYS_TO_PERSIST:
            kwargs.pop(k, None)
        # buffered file
        attributes = {'file': file, 'file_name': file_name}
        _, _, folder = self.http_client.post(path_name, body=attributes, **kwargs)
        return folder

    def destroy(self, file_id):
        """
        Delete a file or folder

        Deletes an existing Inbox
        If the specified Inbox is assigned to any resource, we will remove this Inbox from all such resources
        If the specified Inbox does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /inbox/{file_id}``
        :param int file_id: Unique identifier of a file.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/inbox/{file_id}".format(file_id=file_id))
        return status_code == 204
