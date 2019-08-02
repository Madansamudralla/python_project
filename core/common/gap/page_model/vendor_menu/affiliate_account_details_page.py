from core.common.gap.locators.vendor_menu.affiliate_account_details_page_loc import AffiliateAccountDetailsPageLocators
import core


class AffiliateAccountDetailsPage:
    """This class allows to navigate into the Affiliate Account Details Page"""

    def __init__(self, host):
        self.host = host
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

    def click_save_button_affiliate_details(self):
        """Method to click on Save button

        returns:
            Save latest changes
        """
        self.driver.find_element(*AffiliateAccountDetailsPageLocators.SAVE_BUTTON).click()

    def click_ban_account_button(self):
        """Method to click on Ban account button

        returns:
            Ban account
        """
        self.driver.find_element(*AffiliateAccountDetailsPageLocators.BAN_ACCOUNT_BUTTON).click()

    def click_deactivate_account_button(self):
        """Method to click on Deactivate account button

        returns:
            Deactivate account
        """
        self.driver.find_element(*AffiliateAccountDetailsPageLocators.DEACTIVATE_ACCOUNT_BUTTON).click()
