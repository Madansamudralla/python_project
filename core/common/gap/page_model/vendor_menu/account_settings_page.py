from core.common.gap.locators.vendor_menu.account_settings_page_loc import AccountSettingsPageLocators
import core


class AccounSettingsPage:
    """This class allows to navigate into the Account Settings page and edit some parameters in the page"""
    
    def __init__(self, host):
        self.host = host
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

    def click_save_button_account_settings(self):
        """Method to click on Save button

        returns:
            Save latest changes
        """
        self.driver.find_element(*AccountSettingsPageLocators.SAVE_BUTTON).click()
