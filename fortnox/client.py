from fortnox.configuration import Configuration
from fortnox.http_client import HttpClient

import fortnox.services


class Client(object):
    """
    The :class:`Client <Client>` is the entry point to all services and actions.

    :attribute :class:`Configuration <fortnox.Configuration>` config: Current Fortnox client configuration.
    :attribute :class:`HttpClient <fortnox.HttpClient>` http_client: Http client.

    :copyright: (c) 2020 by Mahmudul Hasan (ikhtiarcse10ruet@gmail.com).
    :license: MIT, see LICENSE for more details.
    """

    def __init__(self, **options):
        """
        Usage::

          >>> import os
          >>> import fortnox
          >>> client = fortnox.Client(access_token=os.environ.get('ACCESS_TOKEN'), client_secret=os.environ.get('CLIENT_SECRET'))
          <fortnox.Client>


        :param str access_token: Personal access token.
        :param str client_secret: Personal access token.
        :param str base_url: (optional) Base url for the api. Default: ``https://api.getbase.com``.
        :param bool verbose: (optional) Verbose/debug mode. Default: ``False``.
        :param int timeout: (optional) Connection and response timeout. Default: **30** seconds.

        :raises ConfigurationError: if no ``access_token`` provided.
        :raises ConfigurationError: if provided ``access_token`` is invalid - contains disallowed characters.
        :raises ConfigurationError: if provided ``access_token`` is invalid - has invalid length.
        :raises ConfigurationError: if provided ``base_url`` is invalid.
        """

        self.config = Configuration(**options)
        self.config.validate()

        self.http_client = HttpClient(self.config)

        self.__customers = fortnox.services.CustomerService(self.http_client)
        self.__company_settings = fortnox.services.CompanySettingsService(self.http_client)

    @property
    def customers(self):
        """
        :return: :class:`CustomerService <fortnox.CustomerService>` object that gives you an access to all Customers related actions.
        :rtype: fortnox.CustomerService
        """
        return self.__customers

    @property
    def company_settings(self):
        """
        :return: :class:`CompanySettingsService <fortnox.CompanySettingsService>` object that gives you an access to CompanySettings related actions.
        :rtype: fortnox.CompanySettingsService
        """
        return self.__company_settings
