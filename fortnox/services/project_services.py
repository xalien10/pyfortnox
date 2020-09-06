class ProjectService(object):
    """
    :class:`fortnox.ProjectService` is used by :class:`fortnox.Client` to make
    actions related to Project resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Project to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['Description', ]
    SERVICE = "Project"

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
        Retrieve all Projects

        Returns all Projects available to the Company, according to the parameters provided

        :calls: ``get /projects``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Projects.
        :rtype: list
        """

        _, _, projects = self.http_client.get("/projects", params=params)
        return projects

    def retrieve(self, number):
        """
        Retrieve a single project

        Returns a single project according to the unique project ID provided
        If the specified project does not exist, this query returns an error

        :calls: ``get /projects/{number}``
        :param int id: Unique identifier of a project.
        :return: Dictionary that support attriubte-style access and represent project resource.
        :rtype: dict
        """
        _, _, project = self.http_client.get("/projects/{number}".format(number=number))
        return project

    def create(self, *args, **kwargs):
        """
        Create a project

        Creates a new project
        **Notice** the project's name **must** be unique within the scope of the resource_type

        :calls: ``post /projects``
        :param tuple *args: (optional) Single object representing project resource.
        :param dict **kwargs: (optional) project attributes.
        :return: Dictionary that support attriubte-style access and represents newely created project resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Project are missing')

        initial_attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in initial_attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, project = self.http_client.post("/projects", body=attributes)
        return project

    def update(self, number, *args, **kwargs):
        """
        Update a Project

        Updates a Project's information
        If the specified Project does not exist, this query will return an error
        **Notice** if you want to update a Project, you **must** make sure the Project's name is unique within the scope of the specified resource

        :calls: ``put /projects/{number}``
        :param int id: Unique identifier of a Project.
        :param tuple *args: (optional) Single object representing Project resource which attributes should be updated.
        :param dict **kwargs: (optional) Project attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Project resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Project are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, customer = self.http_client.put("/projects/{number}".format(number=number), body=attributes)
        return customer

    def destroy(self, number):
        """
        Delete a project

        Deletes an existing project
        If the specified project is assigned to any resource, we will remove this project from all such resources
        If the specified project does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /projects/{number}``
        :param int id: Unique identifier of a project.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/projects/{number}".format(number=number))
        return status_code == 204
