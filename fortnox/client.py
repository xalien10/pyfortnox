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

        self.__access_token = fortnox.services.AccessTokenService(self.http_client)
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
        self.__invoices = fortnox.services.InvoiceService(self.http_client)
        self.__asset_types = fortnox.services.AssetTypeService(self.http_client)
        self.__predefined_accounts = fortnox.services.PredefinedAccountService(self.http_client)
        self.__predefined_voucher_series = fortnox.services.PredefinedVoucherSeriesService(self.http_client)
        self.__assets = fortnox.services.AssetService(self.http_client)
        self.__attendance_transactions = fortnox.services.AttendanceTransactionsService(self.http_client)
        self.__archives = fortnox.services.ArchiveService(self.http_client)
        self.__article_file_connections = fortnox.services.ArticleFileConnectionsService(self.http_client)
        self.__asset_file_connections = fortnox.services.AssetFileConnectionService(self.http_client)
        self.__contract_accruals = fortnox.services.ContractAccrualService(self.http_client)
        self.__contracts = fortnox.services.ContractService(self.http_client)
        self.__contract_templates = fortnox.services.ContractTemplateService(self.http_client)
        self.__cost_centers = fortnox.services.CostCenterService(self.http_client)
        self.__inbox = fortnox.services.InboxService(self.http_client)
        self.__invoice_accruals = fortnox.services.InvoiceAccrualService(self.http_client)
        self.__invoice_payments = fortnox.services.InvoicePaymentService(self.http_client)
        self.__labels = fortnox.services.LabelService(self.http_client)
        self.__locked_periods = fortnox.services.LockedPeriodService(self.http_client)
        self.__modes_of_payments = fortnox.services.ModesOfPaymentService(self.http_client)
        self.__nox_finans_invoices = fortnox.services.NoxFinansInvoiceService(self.http_client)
        self.__offers = fortnox.services.OfferService(self.http_client)
        self.__orders = fortnox.services.OrderService(self.http_client)
        self.__price_lists = fortnox.services.PriceListService(self.http_client)
        self.__prices = fortnox.services.PriceService(self.http_client)
        self.__print_templates = fortnox.services.PrintTemplateService(self.http_client)
        self.__salary_transactions = fortnox.services.SalaryTransactionService(self.http_client)
        self.__schedule_times = fortnox.services.ScheduleTimeService(self.http_client)
        self.__sie = fortnox.services.SIEService(self.http_client)
        self.__supplier_invoice_accruals = fortnox.services.SupplierInvoiceAccrualService(self.http_client)
        self.__supplier_invoice_external_url_connections = fortnox.services.SupplierInvoiceExternalURLConnectionService(
            self.http_client)
        self.__supplier_invoice_file_connections = fortnox.services.SupplierInvoiceFileConnectionService(
            self.http_client)
        self.__supplier_invoice_payments = fortnox.services.SupplierInvoicePaymentService(self.http_client)
        self.__supplier_invoices = fortnox.services.SupplierInvoiceService(self.http_client)
        self.__suppliers = fortnox.services.SupplierService(self.http_client)
        self.__tax_reductions = fortnox.services.TaxReductionService(self.http_client)
        self.__terms_of_deliveries = fortnox.services.TermsOfDeliveryService(self.http_client)
        self.__terms_of_payments = fortnox.services.TermsOfPaymentService(self.http_client)
        self.__email_trusted_domains = fortnox.services.TrustedDomainService(self.http_client)
        self.__trusted_email_senders = fortnox.services.TrustedSenderService(self.http_client)
        self.__units = fortnox.services.UnitService(self.http_client)
        self.__voucher_file_connections = fortnox.services.VoucherFileConnectionService(self.http_client)
        self.__voucher_series = fortnox.services.VoucherSeriesService(self.http_client)
        self.__vouchers = fortnox.services.VoucherService(self.http_client)
        self.__way_of_deliveries = fortnox.services.WayOfDeliveryService(self.http_client)

    @property
    def token(self):
        """
        :return: :class:`AccessTokenService <fortnox.AccessTokenService>` object that gives you an access token that will be used in all other  actions.
        :rtype: fortnox.AccessTokenService
        """
        return self.__access_token

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

    @property
    def invoices(self):
        """
        :return: :class:`InvoiceService <fortnox.InvoiceService>` object that gives you an access to Invoice related actions.
        :rtype: fortnox.InvoiceService
        """
        return self.__invoices

    @property
    def asset_types(self):
        """
        :return: :class:`AssetTypeService <fortnox.AssetTypeService>` object that gives you an access to Asset Type related actions.
        :rtype: fortnox.AssetTypeService
        """
        return self.__asset_types

    @property
    def predefined_accounts(self):
        """
        :return: :class:`PredefinedAccountService <fortnox.PredefinedAccountService>` object that gives you an access to Predefined Accounts related actions.
        :rtype: fortnox.PredefinedAccountService
        """
        return self.__predefined_accounts

    @property
    def predefined_voucher_series(self):
        """
        :return: :class:`PredefinedVoucherSeriesService <fortnox.PredefinedVoucherSeriesService>` object that gives you an access to Predefined Voucher Series related actions.
        :rtype: fortnox.PredefinedVoucherSeriesService
        """
        return self.__predefined_voucher_series

    @property
    def assets(self):
        """
        :return: :class:`AssetService <fortnox.AssetService>` object that gives you an access to Asset related actions.
        :rtype: fortnox.AssetService
        """
        return self.__assets

    @property
    def attendance_transactions(self):
        """
        :return: :class:`AttendanceTransactionsService <fortnox.AttendanceTransactionsService>` object that gives you an access to Attendance Transactions related actions.
        :rtype: fortnox.AttendanceTransactionsService
        """
        return self.__attendance_transactions

    @property
    def archives(self):
        """
        :return: :class:`ArchiveService <fortnox.ArchiveService>` object that gives you an access to Archive Transactions related actions.
        :rtype: fortnox.ArchiveService
        """
        return self.__archives

    @property
    def article_file_connections(self):
        """
        :return: :class:`ArticleFileConnectionsService <fortnox.ArticleFileConnectionsService>` object that gives you an access to Article File Connections related actions.
        :rtype: fortnox.ArticleFileConnectionsService
        """
        return self.__article_file_connections

    @property
    def asset_file_connections(self):
        """
        :return: :class:`AssetFileConnectionService <fortnox.AssetFileConnectionService>` object that gives you an access to Asset File Connection related actions.
        :rtype: fortnox.AssetFileConnectionService
        """
        return self.__asset_file_connections

    @property
    def contract_accruals(self):
        """
        :return: :class:`ContractAccrualService <fortnox.ContractAccrualService>` object that gives you an access to Contract Accrual related actions.
        :rtype: fortnox.ContractAccrualService
        """
        return self.__contract_accruals

    @property
    def contracts(self):
        """
        :return: :class:`ContractService <fortnox.ContractService>` object that gives you an access to Contract related actions.
        :rtype: fortnox.ContractService
        """
        return self.__contracts

    @property
    def contract_templates(self):
        """
        :return: :class:`ContractTemplateService <fortnox.ContractTemplateService>` object that gives you an access to Contract Template related actions.
        :rtype: fortnox.ContractTemplateService
        """
        return self.__contract_templates

    @property
    def cost_centers(self):
        """
        :return: :class:`CostCenterService <fortnox.CostCenterService>` object that gives you an access to Cost Center related actions.
        :rtype: fortnox.CostCenterService
        """
        return self.__cost_centers

    @property
    def invoice_accruals(self):
        """
        :return: :class:`InvoiceAccrualService <fortnox.InvoiceAccrualService>` object that gives you an access to Invoice Accrual related actions.
        :rtype: fortnox.InvoiceAccrualService
        """
        return self.__invoice_accruals

    @property
    def invoice_payments(self):
        """
        :return: :class:`InvoicePaymentService <fortnox.InvoicePaymentService>` object that gives you an access to Invoice Payment related actions.
        :rtype: fortnox.InvoicePaymentService
        """
        return self.__invoice_payments

    @property
    def labels(self):
        """
        :return: :class:`LabelService <fortnox.LabelService>` object that gives you an access to Label related actions.
        :rtype: fortnox.LabelService
        """
        return self.__labels

    @property
    def locked_periods(self):
        """
        :return: :class:`LockedPeriodService <fortnox.LockedPeriodService>` object that gives you an access to Locked Period related actions.
        :rtype: fortnox.LockedPeriodService
        """
        return self.__locked_periods

    @property
    def modes_of_payments(self):
        """
        :return: :class:`ModesOfPaymentService <fortnox.ModesOfPaymentService>` object that gives you an access to Modes Of Payment related actions.
        :rtype: fortnox.ModesOfPaymentService
        """
        return self.__modes_of_payments

    @property
    def nox_finans_invoices(self):
        """
        :return: :class:`NoxFinansInvoiceService <fortnox.NoxFinansInvoiceService>` object that gives you an access to Nox Finans Invoice related actions.
        :rtype: fortnox.NoxFinansInvoiceService
        """
        return self.__nox_finans_invoices

    @property
    def offers(self):
        """
        :return: :class:`OfferService <fortnox.OfferService>` object that gives you an access to Offer related actions.
        :rtype: fortnox.OfferService
        """
        return self.__offers

    @property
    def orders(self):
        """
        :return: :class:`OrderService <fortnox.OrderService>` object that gives you an access to Order related actions.
        :rtype: fortnox.OrderService
        """
        return self.__orders

    @property
    def price_lists(self):
        """
        :return: :class:`PriceListService <fortnox.PriceListService>` object that gives you an access to Price List related actions.
        :rtype: fortnox.PriceListService
        """
        return self.__price_lists

    @property
    def prices(self):
        """
        :return: :class:`PriceService <fortnox.PriceService>` object that gives you an access to Price related actions.
        :rtype: fortnox.PriceService
        """
        return self.__prices

    @property
    def print_templates(self):
        """
        :return: :class:`PrintTemplateService <fortnox.PrintTemplateService>` object that gives you an access to Print Template related actions.
        :rtype: fortnox.PrintTemplateService
        """
        return self.__print_templates

    @property
    def salary_transactions(self):
        """
        :return: :class:`SalaryTransactionService <fortnox.SalaryTransactionService>` object that gives you an access to Salary Transaction related actions.
        :rtype: fortnox.SalaryTransactionService
        """
        return self.__salary_transactions

    @property
    def schedule_times(self):
        """
        :return: :class:`ScheduleTimeService <fortnox.ScheduleTimeService>` object that gives you an access to Schedule Time related actions.
        :rtype: fortnox.ScheduleTimeService
        """
        return self.__schedule_times

    @property
    def sie(self):
        """
        :return: :class:`SIEService <fortnox.SIEService>` object that gives you an access to SIE related actions.
        :rtype: fortnox.SIEService
        """
        return self.__sie

    @property
    def supplier_invoice_accruals(self):
        """
        :return: :class:`SupplierInvoiceAccrualService <fortnox.SupplierInvoiceAccrualService>` object that gives you an access to Supplier Invoice Accrual related actions.
        :rtype: fortnox.SupplierInvoiceAccrualService
        """
        return self.__supplier_invoice_accruals

    @property
    def supplier_invoice_external_url_connections(self):
        """
        :return: :class:`SupplierInvoiceExternalURLConnectionService <fortnox.SupplierInvoiceExternalURLConnectionService>` object that gives you an access to Supplier Invoice External URL Connection related actions.
        :rtype: fortnox.SupplierInvoiceExternalURLConnectionService
        """
        return self.__supplier_invoice_external_url_connections

    @property
    def supplier_invoice_file_connections(self):
        """
        :return: :class:`SupplierInvoiceFileConnectionService <fortnox.SupplierInvoiceFileConnectionService>` object that gives you an access to Supplier Invoice File Connection related actions.
        :rtype: fortnox.SupplierInvoiceFileConnectionService
        """
        return self.__supplier_invoice_file_connections

    @property
    def supplier_invoice_payments(self):
        """
        :return: :class:`SupplierInvoicePaymentService <fortnox.SupplierInvoicePaymentService>` object that gives you an access to Supplier Invoice Payment related actions.
        :rtype: fortnox.SupplierInvoicePaymentService
        """
        return self.__supplier_invoice_payments

    @property
    def supplier_invoices(self):
        """
        :return: :class:`SupplierInvoiceService <fortnox.SupplierInvoiceService>` object that gives you an access to Supplier Invoice related actions.
        :rtype: fortnox.SupplierInvoiceService
        """
        return self.__supplier_invoices

    @property
    def suppliers(self):
        """
        :return: :class:`SupplierService <fortnox.SupplierService>` object that gives you an access to Supplier related actions.
        :rtype: fortnox.SupplierService
        """
        return self.__suppliers

    @property
    def tax_reductions(self):
        """
        :return: :class:`TaxReductionService <fortnox.TaxReductionService>` object that gives you an access to Tax Reduction related actions.
        :rtype: fortnox.TaxReductionService
        """
        return self.__tax_reductions

    @property
    def terms_of_deliveries(self):
        """
        :return: :class:`TermsOfDeliveryService <fortnox.TermsOfDeliveryService>` object that gives you an access to Terms Of Delivery related actions.
        :rtype: fortnox.TermsOfDeliveryService
        """
        return self.__terms_of_deliveries

    @property
    def terms_of_payments(self):
        """
        :return: :class:`TermsOfPaymentService <fortnox.TermsOfPaymentService>` object that gives you an access to Terms Of Payment related actions.
        :rtype: fortnox.TermsOfPaymentService
        """
        return self.__terms_of_payments

    @property
    def email_trusted_domains(self):
        """
        :return: :class:`TrustedDomainService <fortnox.TrustedDomainService>` object that gives you an access to Trusted Domain related actions.
        :rtype: fortnox.TrustedDomainService
        """
        return self.__email_trusted_domains

    @property
    def trusted_email_senders(self):
        """
        :return: :class:`TrustedSenderService <fortnox.TrustedSenderService>` object that gives you an access to Trusted Email Sender related actions.
        :rtype: fortnox.TrustedSenderService
        """
        return self.__trusted_email_senders

    @property
    def units(self):
        """
        :return: :class:`UnitService <fortnox.UnitService>` object that gives you an access to Unit related actions.
        :rtype: fortnox.UnitService
        """
        return self.__units

    @property
    def voucher_file_connections(self):
        """
        :return: :class:`VoucherFileConnectionService <fortnox.VoucherFileConnectionService>` object that gives you an access to Voucher File Connection related actions.
        :rtype: fortnox.VoucherFileConnectionService
        """
        return self.__voucher_file_connections

    @property
    def voucher_series(self):
        """
        :return: :class:`VoucherSeriesService <fortnox.VoucherSeriesService>` object that gives you an access to Voucher Series related actions.
        :rtype: fortnox.VoucherSeriesService
        """
        return self.__voucher_series

    @property
    def vouchers(self):
        """
        :return: :class:`VoucherService <fortnox.VoucherService>` object that gives you an access to Voucher related actions.
        :rtype: fortnox.VoucherService
        """
        return self.__vouchers

    @property
    def way_of_deliveries(self):
        """
        :return: :class:`WayOfDeliveryService <fortnox.WayOfDeliveryService>` object that gives you an access to Way Of Delivery related actions.
        :rtype: fortnox.WayOfDeliveryService
        """
        return self.__way_of_deliveries

    @property
    def inbox(self):
        """
        :return: :class:`InboxService <fortnox.InboxService>` object that gives you an access to Inbox related actions.
        :rtype: fortnox.InboxService
        """
        return self.__inbox
