class SupplierService(object):
    """
    :class:`fortnox.SupplierService` is used by :class:`fortnox.Client` to make
    actions related to Supplier resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Supplier to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Name']
    SERVICE = "Supplier"

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
        Retrieve all Supplier

        Returns all Supplier available to the Company, according to the parameters provided

        :calls: ``get /suppliers``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Supplier.
        :rtype: list
        """

        _, _, suppliers = self.http_client.get("/suppliers", params=params)
        return suppliers

    def retrieve(self, supplier_number):
        """
        Retrieve a single Supplier

        Returns a single Supplier according to the unique Supplier ID provided
        If the specified Supplier does not exist, this query returns an error

        :calls: ``get /suppliers/{supplier_number}``
        :param int id: Unique identifier of a Supplier.
        :return: Dictionary that support attriubte-style access and represent Supplier resource.
        :rtype: dict
        """
        _, _, supplier = self.http_client.get("/suppliers/{supplier_number}".format(supplier_number=supplier_number))
        return supplier

    def create(self, *args, **kwargs):
        """
        Create a Supplier

        Creates a new Supplier
        **Notice** the Supplier's name **must** be unique within the scope of the resource_type

        :calls: ``post /suppliers``
        :param tuple *args: (optional) Single object representing Supplier resource.
        :param dict **kwargs: (optional) supplier attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Supplier resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Supplier are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, supplier = self.http_client.post("/suppliers", body=attributes)
        return supplier

    def update(self, supplier_number, *args, **kwargs):
        """
        Update a Supplier

        Updates a Supplier's information
        If the specified Supplier does not exist, this query will return an error
        **Notice** if you want to update a Supplier, you **must** make sure the Supplier's name is unique within the scope of the specified resource

        :calls: ``put /suppliers/{supplier_number}``
        :param int id: Unique identifier of a Supplier.
        :param tuple *args: (optional) Single object representing Supplier resource which attributes should be updated.
        :param dict **kwargs: (optional) Supplier attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Supplier resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Supplier are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, supplier = self.http_client.put("/suppliers/{supplier_number}".format(supplier_number=supplier_number),
                                              body=attributes)
        return supplier
