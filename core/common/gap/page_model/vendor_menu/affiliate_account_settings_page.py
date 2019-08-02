from core.common.gap.locators.vendor_menu.affiliate_account_settings_page_loc import AffiliateAccountSettingsPageLocators
import core


class AffiliateAccountSettingsPage:
    """This class allows to navigate into the Affiliate Settings Page"""

    def __init__(self, host):
        self.host = host
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

    def click_save_button_affiliate_settings(self):
        """Method to click on Save button

        returns:
            Save latest changes
        """
        self.driver.find_element(*AffiliateAccountSettingsPageLocators.SAVE_BUTTON).click()
