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
        self.__account_charts = fortnox.services.AccountChartsService(self.http_client)
        self.__accounts = fortnox.services.AccountsService(self.http_client)
        self.__absence_transactions = fortnox.services.AbsenceTransactionsService(self.http_client)
        self.__currencies = fortnox.services.CurrencyService(self.http_client)
        self.__company_information = fortnox.services.CompanyInformationService(self.http_client)
        self.__employees = fortnox.services.EmployeeService(self.http_client)
        self.__projects = fortnox.services.ProjectService(self.http_client)
        self.__articles = fortnox.services.ArticleService(self.http_client)
        self.__expenses = fortnox.services.ExpenseService(self.http_client)
        self.__financial_years = fortnox.services.FinancialYearService(self.http_client)

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

    @property
    def account_charts(self):
        """
        :return: :class:`AccountChartsService <fortnox.AccountChartsService>` object that gives you an access to AccountChartsService related actions.
        :rtype: fortnox.AccountChartsService
        """
        return self.__account_charts

    @property
    def accounts(self):
        """
        :return: :class:`AccountsService <fortnox.AccountsService>` object that gives you an access to AccountsService related actions.
        :rtype: fortnox.AccountsService
        """
        return self.__accounts

    @property
    def absence_transactions(self):
        """
        :return: :class:`AbsenceTransactionsService <fortnox.AbsenceTransactionsService>` object that gives you an access to AbsenceTransactionsService related actions.
        :rtype: fortnox.AbsenceTransactionsService
        """
        return self.__absence_transactions

    @property
    def currencies(self):
        """
        :return: :class:`CurrencyService <fortnox.CurrencyService>` object that gives you an access to CurrencyService related actions.
        :rtype: fortnox.CurrencyService
        """
        return self.__currencies

    @property
    def company_information(self):
        """
        :return: :class:`CompanyInformationService <fortnox.CompanyInformationService>` object that gives you an access to CompanyInformationService related actions.
        :rtype: fortnox.CompanyInformationService
        """
        return self.__company_information

    @property
    def employees(self):
        """
        :return: :class:`EmployeeService <fortnox.EmployeeService>` object that gives you an access to Employees related actions.
        :rtype: fortnox.EmployeeService
        """
        return self.__employees

    @property
    def projects(self):
        """
        :return: :class:`ProjectService <fortnox.ProjectService>` object that gives you an access to Projects related actions.
        :rtype: fortnox.ProjectService
        """
        return self.__projects

    @property
    def articles(self):
        """
        :return: :class:`ArticleService <fortnox.ArticleService>` object that gives you an access to Articles related actions.
        :rtype: fortnox.ArticleService
        """
        return self.__articles

    @property
    def expenses(self):
        """
        :return: :class:`ExpenseService <fortnox.ExpenseService>` object that gives you an access to Expense related actions.
        :rtype: fortnox.ExpenseService
        """
        return self.__expenses

    @property
    def financial_years(self):
        """
        :return: :class:`FinancialYearService <fortnox.FinancialYearService>` object that gives you an access to Financial Year related actions.
        :rtype: fortnox.FinancialYearService
        """
        return self.__financial_years
