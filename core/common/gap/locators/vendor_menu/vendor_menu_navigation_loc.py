from selenium.webdriver.common.by import By


class VendorMenuPageLocators:

    # Account Overview
    ACCOUNT_DETAILS_LINKTEXT = By.LINK_TEXT,'Account details'
    ACCOUNT_SETTINGS_LINKTEXT = By.LINK_TEXT, 'Account settings'
    PAYMENT_OPTIONS_LINKTEXT = By.LINK_TEXT, 'Payment options'
    AUTOFILL_ACCOUNT_SERVICE_LINKTEXT = By.LINK_TEXT, 'Autofill Account Service'
    TRANSFER_SETTINGS_LINKTEXT = By.LINK_TEXT, 'Transfer settings'
    COMMISSIONS_LINKTEXT = By.LINK_TEXT, 'Commissions'
    CUSTOM_TAXES_LINKTEXT = By.LINK_TEXT, 'Custom taxes'
    LOGIN_LOG_LINKTEXT = By.LINK_TEXT, 'Login log'
    ANTIFRAUD_SETTINGS_LINKTEXT = By.LINK_TEXT, 'Anti-fraud settings'
    SECURE_SETTINGS_LINKTEXT = By.LINK_TEXT, '3DSecure settings'
    FILES_LINKTEXT = By.LINK_TEXT, 'Files'
    PARTENER_LIST_LINKTEXT = By.LINK_TEXT, 'Partner list'
    VAULT_DATA_PURGE_SETTINGS_LINKTEXT = By.LINK_TEXT, 'Vault data purge settings'

    # Vendor Risk
    LPU_STATS_LINKTEXT = By.LINK_TEXT, 'LPU Stats'
    ACCOUNT_MONITORING_FLAGS_LINKTEXT = By.LINK_TEXT, 'Account monitoring flags'
    PAYOUT_CHANGE_REQUEST_LINKTEXT = By.LINK_TEXT, 'Payout change requests'

    # Reports
    ORDERS_REPORTS_LINKTEXT = By.LINK_TEXT, 'Orders reports'
    TRANSACTED_VOLUMES_LINKTEXT = By.LINK_TEXT, 'Transacted volumes'
    MONTHLY_ORDERS_LINKTEXT = By.LINK_TEXT, 'Monthly orders'

    # Underwriting
    ACCOUNT_STATUS_LINKTEXT = By.LINK_TEXT, 'Account status'
    ACCOUNT_LINKING_TOOL_LINKTEXT = By.LINK_TEXT, 'Account linking tool'
