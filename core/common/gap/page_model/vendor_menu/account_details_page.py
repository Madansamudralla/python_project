from core.common.gap.locators.vendor_menu.account_details_page_loc import AccountDetailsPageLocators
import core


class AccountDetailsPage:
    """This class allows to navigate into the Account Details page and edit some parameters in the page"""

    def __init__(self, host):
        self.host = host
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

    def click_save_button_account_details(self):
        """Method to click on Save button

        returns:
            Save latest changes
        """
        self.driver.find_element(*AccountDetailsPageLocators.SAVE_BUTTON_INPUT).click()
