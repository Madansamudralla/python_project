from selenium.webdriver.common.by import By


class AccountSettingsPageLocators:

    RESTRICTED_ACCOUNT_TO_ONE_PAYOUT_OPTION_CHECKBOX = By.NAME, 'IsRestrictedToOnePayoutOption'
    VENDOR_TO_VENDOR_PAYMENTS_CHECKBOX = By.ID, 'package_149'
    AFFILIATES_NETWORK_CHECKBOX = By.ID, 'package_8'
    AFFILIATES_NETWORK_POXA_CHECKBOX = By.ID, 'package_51'
    AFFILIATES_BONUSES_CHECKBOX = By.ID, 'package_29'
    AUTOMATED_FAKE_INVOICES_CHECKBOX = By.ID, 'automatedAccountingPaymentInvoices'
    DISABLE_AGGREGATED_FAKE_INVOICES_CHECKBOX =  By.ID, 'disableAggregatedPaymentInvoices'
    AUTOMATED_SERVICE_INVOICES_CHECKBOX = By.ID, 'automatedAccountingServiceInvoices'
    COMPENSATE_FAKE_INVOICES_CHECKBOX = By.ID, 'compensateServiceInvoicesWithPayments'
    DISPLAY_ESTIMATED_BALANCE_PAGE_CPANEL_CHECKBOX = By.ID, 'package_140'
    GOLIVE_DATE_INPUTDATE = By.ID, 'golivedate'
    SALESFORCE_CONNECTOR_CHECKBOX = By.ID, 'package_39'
    CONFIGURABLE_EVENTS_CHECKBOX = By.ID, 'package_89'
    COMMISSION_INVOICES_CHECKBOX = By.NAME, 'invoice'
    SAVE_BUTTON = By.CLASS_NAME, 'submit_accounts_edit_form'
