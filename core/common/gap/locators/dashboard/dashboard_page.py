from selenium.webdriver.common.by import By


class DashboardPageLocators:

    # Menu navigation locators
    HOME_TAB_DASHBOARD = By.LINK_TEXT, 'Home'
    MERCHANTS_TAB_DASHBOARD = By.LINK_TEXT, 'Merchants'
    AFFILIATES_TAB_DASHBOARD = By.LINK_TEXT, 'Affiliates'
    ONLINE_ORDERS_TAB_DASHBOARD = By.LINK_TEXT, 'Online Orders'
    TRANSACTIONS_TAB_DASHBOARD = By.LINK_TEXT, 'Transactions'
    ACCOUNTING_TAB_DASHBOARD = By.LINK_TEXT, 'Accounting'
    REPORTS_TAB_DASHBOARD = By.LINK_TEXT, 'Reports'
    TOOLS_TAB_DASHBOARD = By.LINK_TEXT, 'Tools'
    SETTINGS_TAB_DASHBOARD = By.LINK_TEXT, 'Settings'
    SEARCH_TAB_DASHBOARD = By.LINK_TEXT, 'Search'
    ERRORS_TAB_DASHBOARD = By.LINK_TEXT, 'Errors'
    VENDOR_TAB_DASHBOARD_ALERTS = By.LINK_TEXT, 'Vendor Alerts'

    GAP_SEARCH_INPUT = By.ID, 'tiSearch'
