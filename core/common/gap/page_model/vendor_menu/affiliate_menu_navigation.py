from core.common.gap.locators.vendor_menu.affiliate_menu_navigation_loc import AffiliateMenuNavigationLocators
import core


class AffiliateMeniuNavigationPage:
    """This class allows to navigate into the Affiliate Menu Navigation"""

    def __init__(self, host):
        self.host = host
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

    # Account details
    def click_amenu_account_details(self):
        """Method to go on Account details link

        returns:
            Account details page
        """
        self.driver.find_element(*AffiliateMenuNavigationLocators.ACCOUNT_DETAILS_LINKTEXT).click()

    def click_amenu_account_settings(self):
        """Method to go on Account settings link

        returns:
            Account settings page
        """
        self.driver.find_element(*AffiliateMenuNavigationLocators.ACCOUNT_SETTINGS_LINKTEXT).click()

    def click_amenu_power_affiliate_settings(self):
        """Method to go on Power affiliate settings link

        returns:
            Power affiliate settings page
        """
        self.driver.find_element(*AffiliateMenuNavigationLocators.POWER_AFFILIATE_SETTINGS_LINKTEXT).click()

    def click_amenu_login_log(self):
        """Method to go on Login log link

        returns:
            Login log page
        """
        self.driver.find_element(*AffiliateMenuNavigationLocators.LOGIN_LOG_LINKTEXT).click()

    def click_amenu_files(self):
        """Method to go on Files link

        returns:
            Files page
        """
        self.driver.find_element(*AffiliateMenuNavigationLocators.FILES_LINKTEXT).click()

    def click_amenu_kyc_documents(self):
        """Method to go on Kyc documents link

        returns:
            Kyc documents page
        """
        self.driver.find_element(*AffiliateMenuNavigationLocators.KYC_DOCUMENTS_LINKTEXT).click()

    def click_amenu_custom_taxes_(self):
        """Method to go on Detailed report link

        returns:
            Detailed report page
        """
        self.driver.find_element(*AffiliateMenuNavigationLocators.DETAILED_REPORT_LINKTEXT).click()
