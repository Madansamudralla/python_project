from selenium.webdriver.common.by import By


class AccountDetailsPageLocators:

    SOCRATE_CODE_INPUT = By.NAME, 'socratecode'
    EMAIL_TEMPLATE_SELECT = By.NAME, 'emailtemplate'
    ORDERING_INTERFACE_SELECT = By.ID, 'interface'
    ACCOUNT_TYPE_SELECT = By.ID, 'accountTypes'
    BUSINESS_COMPANY_SELECT = By.NAME, 'IdBusinessCompanies'
    INVOICE_CURRENCY_SELECT = By.NAME, 'IdCurrencyInvoice'
    CHARGEBACK_FUNDS_INPUT =  By.NAME, 'creditline'
    CHARGEBACK_FUNDS_SET_CURRENCY_SELECT = By.NAME, 'creditline'
    SAVE_BUTTON_INPUT = By.CLASS_NAME, 'submit_accounts_edit_form'
