from selenium.webdriver.common.by import By


class DashboardPageLocators:

    HOME_PAGE_BUTTON = By.CLASS_NAME, 'logo 2MONETIZE pull-left'

    # MENU ITEM
    M_SETUP = By.XPATH, '/html/body/aside/ul/li[2]/div/span/i'
    # M_SETUP = By.ID, 'parent_PRODUCTS'

    # Submenu items
    SM_PRODUCTS = By.ID, 'submenu-child-item-EDIT_PRODUCTS'
    SM_FULFILLMENT = By.ID, 'submenu-child-item-ELECTRONIC'
    SM_PRICE_LISTS = By.ID, 'submenu-child-item-PRICE_LISTS'
    SM_RENEWAL = By.ID, 'submenu-child-item-OVERVIEW'
    SM_GENERATE_LINKS = By.ID, 'submenu-child-item-SALES_LINKS'
    SM_INTERFACE_TEMPLATES = By.ID, 'submenu-child-item-TEMPLATES'
    SM_ORDERING_OPTIONS = By.ID, 'submenu-child-item-ORDER_SETTINGS'
    SM_PARTNER_INVOICE_SETTINGS = By.ID, 'submenu-child-item-PARTNER_INVOICE_SETTINGS'
    SM_MEDIA_CENTER = By.ID, 'submenu-child-item-MEDIA_CENTER'

    # MENU ITEM
    M_MARKETING_TOOLS = By.ID, 'parent_MARKETING_TOOLS'

    # Submenu items
    SM_OVERVIEW = By.ID, 'submenu-child-item-INDEX_MARKETING'
    SM_PROMOTIONS = By.ID, 'submenu-child-item-PROMOTIONS'
    SM_CROSS_SELLING = By.ID, 'submenu-child-item-CROSS_SELLING'
    SM_UPSELLING = By.ID, 'submenu-child-item-UP_SELLING'
    SM_RETENTION_TOOLS = By.ID, 'submenu-child-item-RETENTION_TOOLS'
    SM_EMAIL_MARKETING = By.ID, 'submenu-child-item-EMAIL_MARKETING'
    SM_LEAD_MANAGEMENT = By.ID, 'submenu-child-item-LEADS_MANAGEMENT'
    SM_AB_TESTING = By.ID, 'submenu-child-item-ABTESTING'
    SM_EMAIL_EDITOR = By.ID, 'submenu-child-item-TEMPLATE_MANAGER'
    SM_CHANNEL_RESOURCES = By.ID, 'submenu-child-item-RESOURCES_AFFILIATES'

    # MENU ITEM
    M_AFFILIATE_NETWORK = By.ID, 'parent_AFFILIATES_NETWORK'

    # Submenu items
    SM_SETTINGS = By.ID, 'submenu-child-item-AFFILIATES'
    SM_RELATIONSHIPS = By.ID, 'submenu-child-item-RELATIONS'
    SM_BUILD_YOUR_NETWORK = By.ID, 'submenu-child-item-AFF_LINKS'
    SM_POWER_AFFILIATES = By.ID, 'submenu-child-item-AFFILIATE_OPPORTUNITIES'
    SM_NEWSLETTER = By.ID, 'submenu-child-item-NEWSLETTER'
    SM_BONUS_PROGRAMS = By.ID, 'submenu-child-item-ROYALTY_FEES'

    # MENU ITEM
    M_PARTNER_MANAGEMENT = By.ID, 'parent_PARTNERS'

    # Submenu items
    SM_PARTNERS = By.ID, 'submenu-child-item-LIST_RESELLERS'
    SM_PARTNERSHIP_PROGRAMS = By.ID, 'submenu-child-item-LIST_PARTNERSHIP_PROGRAMS'

    # MENU ITEM
    M_ORDERS_CUSTOMERS = By.ID, 'parent_ORDERS'

    # Submenu items
    SM_ORDER_SEARCH = By.ID, 'submenu-child-item-SEARCH'
    SM_PLACE_PARTNER_ORDER = By.ID, 'submenu-child-item-RESELLER_ADD_ORDER'
    SM_PURCHASE_ORDERS = By.ID, 'submenu-child-item-PO'
    SM_FULFILLMENT_CONFIRMATIONS = By.ID, 'submenu-child-item-DELIVERY'
    SM_PARTNER_INVOICES = By.ID, 'submenu-child-item-PARTNERS_LIST_INVOICES'
    SM_CUSTOMERS = By.ID, 'submenu-child-item-CUSTOMERS_MANAGEMENT'
    SM_SUBSCRIPTIONS = By.ID, 'submenu-child-item-LICENSE_MAGEMENT'
    SM_REFUNDS = By.ID, 'submenu-child-item-REFUNDS'

    # MENU ITEM
    M_INTEGRATIONS = By.ID, 'parent_INTEGRATIONS_WEBHOOKS_API'

    # Submenu items
    SM_WEBHOOKS_API = By.ID, 'submenu-child-item-WEBHOOKS_API'
    SM_SALESFORCE_INTEGRATION = By.ID, 'submenu-child-item-SALESFORCE_SETTINGS'
    SM_APPS_PLUGINS = By.ID, 'submenu-child-item-THIRD_PARTY_APPS'

    # MENU ITEM
    M_REPORTS_CENTER = By.ID, 'parent_REPORT_CENTER'

    # Submenu items
    SM_MAIN_REPORTS = By.ID, 'submenu-child-item-MAIN_REPORTS'
    SM_CUSTOM_REPORTS = By.ID, 'submenu-child-item-CUSTOM_REPORTS'
    SM_USERS_ACTIVITY = By.ID, 'submenu-child-item-USERS_LOGS'
    SM_AUTHORIZATION_REPORT = By.ID, 'submenu-child-item-AUTHORIZATIONS_REPORT'
    SM_API_WEBHOOKS = By.ID, 'submenu-child-item-API_NOTIF_LOGS'

    # # MENU ITEM
    # M_ACCOUNT_SETTINGS = By.ID, 'parent_ACCOUNT_SETTINGS'
    #
    # # Submenu items
    # SM_ACCOUNT_INFORMATION = By.ID, 'submenu-child-item-ACC_INFO'
    # SM_LOGIN_INFORMATION = By.ID, 'submenu-child-item-LOGIN_INFO'
    # SM_SYSTEM_SETTINGS = By.ID, 'submenu-child-item-SYS_SETTINGS'
    # SM_FINANCIAL_DETAILS = By.ID, 'submenu-child-item-FINANCIAL'
    # SM_USER_ACCESS = By.ID, 'submenu-child-item-USERS_ACCESS'
    # SM_USERS_ACTIVITY = By.ID, 'submenu-child-item-USERS_LOGS'
    # SM_RESOURCES = By.ID, 'parent_RESOURCES'
    # SM_HELP = By.ID, 'submenu-child-item-HELP'

    # MENU ITEM
    M_ACCOUNTING = By.ID, 'parent_ACCOUNTING'
    # Submenu items
    SM_ESTIMATED_BALANCE = By.ID, 'submenu-child-item-ESTIMATED_BALANCE'
    SM_PAYMENTS = By.ID, 'submenu-child-item-ACCOUNTING_PAYMENTS'
    SM_FINANCE_DOCUMENTS = By.ID, 'submenu-child-item-ACCOUNTING_INVOICES'

    # DASHBOARD GENERIC PAGE ITEMS
    PAGE_TITLE = By.ID, 'page-title'
    TOP_BOX = By.ID, 'top-box'
    SETUP_PRODUCTS_BUTTON = By.CLASS_NAME, 'btn btn-primary'
    CONTACT_US = By.ID, 'liveChatStatusImage'
