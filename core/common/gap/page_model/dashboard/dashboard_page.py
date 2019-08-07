from selenium.webdriver.common.keys import Keys
from core.common.gap.locators.dashboard.dashboard_page import DashboardPageLocators
import core


class DashboardPage:

    def __init__(self, host):
        self.host = host
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

    def go_to_home_dashboard(self):
        """Method to go on HOME dashboard link

        returns:
            Home page
        """
        self.driver.find_element(*DashboardPageLocators.HOME_TAB_DASHBOARD).click()

    def go_to_merchants_dashboard(self):
        """Method to go on Merchants dashboard link

        returns:
            Merchants page
        """
        self.driver.find_element(*DashboardPageLocators.MERCHANTS_TAB_DASHBOARD).click()

    def go_to_affiliates_dashboard(self):
        """Method to go on Affiliates dashboard link

        returns:
            Affiliates page
        """
        self.driver.find_element(*DashboardPageLocators.AFFILIATES_TAB_DASHBOARD).click()

    def go_to_online_orders_dashboard(self):
        """Method to go on Online Orders dashboard link

        returns:
            Online Orders
        """
        self.driver.find_element(*DashboardPageLocators.ONLINE_ORDERS_TAB_DASHBOARD).click()

    def go_to_transactions_dashboard(self):
        """Method to go on Transactions dashboard link

        returns:
            Transactions page
        """
        self.driver.find_element(*DashboardPageLocators.TRANSACTIONS_TAB_DASHBOARD).click()

    def go_to_accounting_dashboard(self):
        """Method to go on Accounting dashboard link

        returns:
            Accounting page
        """
        self.driver.find_element(*DashboardPageLocators.ACCOUNTING_TAB_DASHBOARD).click()

    def go_to_reports_dashboard(self):
        """Method to go on Reports dashboard link

        returns:
            Reports page
        """
        self.driver.find_element(*DashboardPageLocators.REPORTS_TAB_DASHBOARD).click()

    def go_to_tools_dashboard(self):
        """Method to go on Tools dashboard link

        returns:
            Tools page
        """
        self.driver.find_element(*DashboardPageLocators.TOOLS_TAB_DASHBOARD).click()

    def go_to_settings_dashboard(self):
        """Method to go on Settings dashboard link

        returns:
            Settings page
        """
        self.driver.find_element(*DashboardPageLocators.SETTINGS_TAB_DASHBOARD).click()

    def go_to_search_dashboard(self):
        """Method to go on Search dashboard link

        returns:
            Search page
        """
        self.driver.find_element(*DashboardPageLocators.SEARCH_TAB_DASHBOARD).click()

    def go_to_errors_dashboard(self):
        """Method to go on Errors dashboard link

        returns:
            Errors page
        """
        self.driver.find_element(*DashboardPageLocators.ERRORS_TAB_DASHBOARD).click()

    def go_to_vendor_alerts_dashboard(self):
        """Method to go on Vendor Alerts dashboard link

        returns:
            Vendor Alerts page
        """
        self.driver.find_element(*DashboardPageLocators.VENDOR_TAB_DASHBOARD_ALERTS).click()

    def fill_gap_search_for_something(self, gapsearch):
        """Method to go on SEARCH GAP dashboard link

        returns:
            SEARCH GAP page
        """
        self.driver.find_element(*DashboardPageLocators.GAP_SEARCH_INPUT).send_keys(gapsearch)
        self.driver.find_element(*DashboardPageLocators.GAP_SEARCH_INPUT).send_keys(Keys.ENTER)
