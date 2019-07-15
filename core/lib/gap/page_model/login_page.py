from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.convert_plus.locators.checkout_page import CheckoutPageLocators
from selenium.webdriver.common.keys import Keys
import core


class GapLogin:

    def __init__(self):
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver
