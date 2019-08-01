from core.common.gap.locators.vendor_menu.vendor_menu_navigation_loc import VendorMenuPageLocators
import core


class VendorMenuPage:
    """This class allows to navigate into the Vendor Menu Navigation"""

    def __init__(self, host):
        self.host = host
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

    # Account Overview
    def click_vmenu_account_details(self):
        """Method to go on Account details link

        returns:
            Account details page
        """
        self.driver.find_element(*VendorMenuPageLocators.ACCOUNT_DETAILS_LINKTEXT).click()

    def click_vmenu_account_settings(self):
        """Method to go on Account settings link

        returns:
            Account settings page
        """
        self.driver.find_element(*VendorMenuPageLocators.ACCOUNT_SETTINGS_LINKTEXT).click()

    def click_vmenu_payment_option(self):
        """Method to go on Payment options link

        returns:
            Payment options page
        """
        self.driver.find_element(*VendorMenuPageLocators.PAYMENT_OPTIONS_LINKTEXT).click()

    def click_vmenu_autofill_account_service(self):
        """Method to go on Autofill Account Service link

        returns:
            Autofill Account Service page
        """
        self.driver.find_element(*VendorMenuPageLocators.AUTOFILL_ACCOUNT_SERVICE_LINKTEXT).click()

    def click_vmenu_transfer_settings(self):
        """Method to go on Transfer settings link

        returns:
            Transfer settings page
        """
        self.driver.find_element(*VendorMenuPageLocators.TRANSFER_SETTINGS_LINKTEXT).click()

    def click_vmenu_commissions(self):
        """Method to go on Commissions link

        returns:
            Commissions page
        """
        self.driver.find_element(*VendorMenuPageLocators.COMMISSIONS_LINKTEXT).click()

    def click_vmenu_custom_taxes_(self):
        """Method to go on Custom taxes link

        returns:
            Custom taxes page
        """
        self.driver.find_element(*VendorMenuPageLocators.CUSTOM_TAXES_LINKTEXT).click()

    def click_vmenu_login_log(self):
        """Method to go on Login log link

        returns:
            Login log page
        """
        self.driver.find_element(*VendorMenuPageLocators.LOGIN_LOG_LINKTEXT).click()

    def click_vmenu_antifraud_settings(self):
        """Method to go on Anti-fraud settings link

        returns:
            Anti-fraud settings page
        """
        self.driver.find_element(*VendorMenuPageLocators.ANTIFRAUD_SETTINGS_LINKTEXT).click()

    def click_vmenu_secure_settings(self):
        """Method to go on 3DSecure settings link

        returns:
            3DSecure settings page
        """
        self.driver.find_element(*VendorMenuPageLocators.SECURE_SETTINGS_LINKTEXT).click()

    def click_vmenu_files(self):
        """Method to go on Files link

        returns:
            Files page
        """
        self.driver.find_element(*VendorMenuPageLocators.FILES_LINKTEXT).click()

    def click_vmenu_partener_list(self):
        """Method to go on Partner list link

        returns:
            Partner list
        """
        self.driver.find_element(*VendorMenuPageLocators.PARTENER_LIST_LINKTEXT).click()

    def click_vmenu_vault_data_purge_settings(self):
        """Method to go on Vault data purge settings link

        returns:
            Vault data purge settings page
        """
        self.driver.find_element(*VendorMenuPageLocators.VAULT_DATA_PURGE_SETTINGS_LINKTEXT).click()

    # Vendor Risk
    def click_vmenu_lpu_stats(self):
        """Method to go on LPU Stats link

        returns:
            LPU Stats page
        """
        self.driver.find_element(*VendorMenuPageLocators.LPU_STATS_LINKTEXT).click()

    def click_vmenu_account_monitoring_flags(self):
        """Method to go on Account monitoring flags link

        returns:
            Account monitoring flags page
        """
        self.driver.find_element(*VendorMenuPageLocators.ACCOUNT_MONITORING_FLAGS_LINKTEXT).click()

    def click_vmenu_payout_change_request(self):
        """Method to go on Payout change requests link

        returns:
            Payout change requests page
        """
        self.driver.find_element(*VendorMenuPageLocators.PAYOUT_CHANGE_REQUEST_LINKTEXT).click()

    # Reports
    def click_vmenu_orders_reports(self):
        """Method to go on Orders reports link

        returns:
            Orders reports page
        """
        self.driver.find_element(*VendorMenuPageLocators.ORDERS_REPORTS_LINKTEXT).click()

    def click_vmenu_transacted_volumes(self):
        """Method to go on Transacted volumes link

        returns:
            Transacted volumes page
        """
        self.driver.find_element(*VendorMenuPageLocators.TRANSACTED_VOLUMES_LINKTEXT).click()

    def click_vmenu_monthly_orders(self):
        """Method to go on Monthly orders link

        returns:
            Monthly orders page
        """
        self.driver.find_element(*VendorMenuPageLocators.MONTHLY_ORDERS_LINKTEXT).click()

    # Underwriting
    def click_vmenu_account_status(self):
        """Method to go on Account status link

        returns:
            Account status page
        """
        self.driver.find_element(*VendorMenuPageLocators.ACCOUNT_STATUS_LINKTEXT).click()

    def click_vmenu_account_linking_tool(self):
        """Method to go on Account linking tool link

        returns:
            Account linking tool page
        """
        self.driver.find_element(*VendorMenuPageLocators.ACCOUNT_LINKING_TOOL_LINKTEXT).click()
