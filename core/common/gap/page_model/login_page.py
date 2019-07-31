from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from core.common.gap.locators.login_page import GapLoginPageLocators
from core.common.gap.locators.dashboard_page import DashboardPageLocators
from selenium.common.exceptions import NoSuchElementException
import core


class GapLogin:
    """This class allows to login into the GAP with credentials"""
    TIME_SEC = 5

    def __init__(self, host):

        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver
        self.host = host
        self.access_login_page()

    def access_login_page(self):
        """Method to get the current URL

        returns:
          URL as a String object if exist
        """

        self.driver.get(f"{self.host}/admin/")

    def login_to_gap(self, username="automation", password="test123#"):
        """Method to login to the GAP

        returns:
          GAP home page when authentication successful otherwise throws exception
        """

        try:
            self.driver.find_element(*GapLoginPageLocators.USERNAME).is_displayed()
        except NoSuchElementException:
            logging.info("Username input field is not present in the page.")
        logging.info(f"Send username to input field: {username}")
        self.driver.find_element(*GapLoginPageLocators.USERNAME).send_keys(username)

        try:
            self.driver.find_element(*GapLoginPageLocators.PASSWORD).is_displayed()
        except NoSuchElementException:
            logging.info("Password input field is not present in the page.")
        logging.info(f"Send password to input field: {password}")
        self.driver.find_element(*GapLoginPageLocators.PASSWORD).send_keys(password)

        logging.info(f"Click on login button.")
        self.driver.find_element(*GapLoginPageLocators.LOGIN_BUTTON).click()
        logging.info(f"Wait for dashboard page to load.")
        assert WebDriverWait(self.driver, self.TIME_SEC).until(
            EC.presence_of_element_located(DashboardPageLocators.GAP_SEARCH_INPUT))






