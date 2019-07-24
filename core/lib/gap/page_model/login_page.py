from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.lib.gap.locators.login_page_loc import GapLoginPageLocators
import core


class GapLogin:
    """This class allows to login into the GAP with credentials"""
    TIME_SEC = 5

    def __init__(self, host):
        self.host = host
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

    def access_login_page(self):
        """Method to get the current URL

        returns:
          URL as a String object if exist
        """
        self.driver.get(self.host)

    def enter_username(self, username):
        """Method to fill username

        args:
          :username str: email or username
        """
        self.driver.find_element(*GapLoginPageLocators.USERNAME).send_keys(username)

    def enter_password(self, password):
        """Method to fill password

        args:
          :password str: user password
        """
        self.driver.find_element(*GapLoginPageLocators.PASSWORD).send_keys(password)

    def click_login_button(self):
        """Method to click on login button

        returns:
          GAP home page when authentication successful
        """
        self.driver.find_element(*GapLoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(self.driver, self.TIME_SEC).until(
            EC.presence_of_element_located(GapLoginPageLocators.MAINSCROLL_CONTAINER))

        global_administration_panel = self.driver.find_element(*GapLoginPageLocators.MAINSCROLL_CONTAINER).text()
        assert global_administration_panel == 'Avangate eCommerce - Global Administration Panel', \
            'Login failed, please verify your login credentials.'

    def login_to_gap(self, username, password):
        """Method to login to the GAP"""
        self.driver.get(self.host)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
