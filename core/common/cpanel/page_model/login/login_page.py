from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from core.common.cpanel.locators.login.login_page import CpanelLoginPageLocators
from selenium.common.exceptions import NoSuchElementException
import core


class CpanelLogin:
    """This class allows to login into the CPANEL with credentials"""
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

        self.driver.get(f"{self.host}/cpanel/")

    def login_to_cpanel(self, username, password):
        """Method to login to the CPANEL

        returns:
          CPANEL home page when authentication successful otherwise throws exception
        """

        try:
            self.driver.find_element(*CpanelLoginPageLocators.USERNAME).is_displayed()
        except NoSuchElementException:
            logging.info("Username input field is not present in the page.")
        logging.info(f"Send username to input field: {username}")
        self.driver.find_element(*CpanelLoginPageLocators.USERNAME).send_keys(username)

        try:
            self.driver.find_element(*CpanelLoginPageLocators.PASSWORD).is_displayed()
        except NoSuchElementException:
            logging.info("Password input field is not present in the page.")
        logging.info(f"Send password to input field: {password}")
        self.driver.find_element(*CpanelLoginPageLocators.PASSWORD).send_keys(password)

        logging.info(f"Click on login button.")
        self.driver.find_element(*CpanelLoginPageLocators.LOGIN_BUTTON).click()
        logging.info(f"Wait for dashboard page to load.")

        assert WebDriverWait(self.driver, self.TIME_SEC).until(
            EC.presence_of_element_located(CpanelLoginPageLocators.DASHBOARD))
