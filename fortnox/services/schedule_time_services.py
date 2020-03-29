class ScheduleTimeService(object):
    """
    :class:`fortnox.ScheduleTimeService` is used by :class:`fortnox.Client` to make
    actions related to ScheduleTime resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for ScheduleTime to send to Fortnox backend servers.
    """
    OPTS_KEYS_TO_PERSIST = []
    SERVICE = "ScheduleTime"

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
        Retrieve all ScheduleTime

        Returns all ScheduleTime available to the Company, according to the parameters provided

        :calls: ``get /scheduletimes``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of ScheduleTime.
        :rtype: list
        """

        _, _, schedule_times = self.http_client.get("/scheduletimes", params=params)
        return schedule_times

    def retrieve(self, employee_id, date):
        """
        Retrieve a single ScheduleTime

        Returns a single ScheduleTime according to the unique ScheduleTime ID provided
        If the specified ScheduleTime does not exist, this query returns an error

        :calls: ``get /scheduletimes/{employee_id}/{date}``
        :param int id: Unique identifier of a ScheduleTime.
        :return: Dictionary that support attriubte-style access and represent ScheduleTime resource.
        :rtype: dict
        """
        _, _, schedule_time = self.http_client.get(
            "/scheduletimes/{employee_id}/{date}".format(employee_id=employee_id, date=date))
        return schedule_time

    def update(self, employee_id, date, *args, **kwargs):
        """
        Update a ScheduleTime

        Updates a ScheduleTime's information
        If the specified ScheduleTime does not exist, this query will return an error
        **Notice** if you want to update a ScheduleTime, you **must** make sure the ScheduleTime's name is unique within the scope of the specified resource

        :calls: ``put /scheduletimes/{employee_id}/{date}``
        :param int id: Unique identifier of a ScheduleTime.
        :param tuple *args: (optional) Single object representing ScheduleTime resource which attributes should be updated.
        :param dict **kwargs: (optional) ScheduleTime attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated ScheduleTime resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for ScheduleTime are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.items())
        attributes.update({'service': self.SERVICE})
        _, _, schedule_time = self.http_client.put(
            "/scheduletimes/{employee_id}/{date}".format(employee_id=employee_id, date=date), body=attributes)
        return schedule_time

    def reset_day(self, employee_id, date):
        """
        Delete a ScheduleTime

        Deletes an existing ScheduleTime
        If the specified ScheduleTime is assigned to any resource, we will remove this ScheduleTime from all such resources
        If the specified ScheduleTime does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /scheduletimes/{employee_id}/{date}/resetday``
        :param int id: Unique identifier of a ScheduleTime.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        _, _, schedule_time = self.http_client.put(
            "/scheduletimes/{employee_id}/{date}/resetday".format(employee_id=employee_id, date=date))
        return schedule_time
