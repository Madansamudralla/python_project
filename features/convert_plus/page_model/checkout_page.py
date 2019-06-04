from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.convert_plus.locators.checkout_page import CheckoutPageLocators
from selenium.webdriver.common.keys import Keys
from features.convert_plus.page_model.thank_you_page import ThankYouPage


class CheckoutPage:
    TIME_SEC = 30

    def __init__(self, driver):
        self.driver = driver

    def wait_for_loader_to_disappear(self):
        WebDriverWait(self.driver, self.TIME_SEC).until(
            EC.presence_of_element_located(CheckoutPageLocators.LOADER_CLASS_BUSY))

        WebDriverWait(self.driver, self.TIME_SEC).until(
            EC.invisibility_of_element_located(CheckoutPageLocators.LOADER_CLASS_LOCATOR))

    def fill_email_address(self, email):
        self.driver.find_element(*CheckoutPageLocators.EMAIL_INPUT_LOCATOR).send_keys(email)

    def fill_country(self, country):
        self.driver.find_element(*CheckoutPageLocators.COUNTRY_INPUT_LOCATOR).click()
        self.driver.find_element(*CheckoutPageLocators.COUNTRY_INPUT_FIELD).send_keys(country)
        self.driver.find_element(*CheckoutPageLocators.COUNTRY_INPUT_FIELD).send_keys(Keys.ENTER)

    def fill_cc_details(self, cc_number, date, cvv):
        self.driver.find_element(*CheckoutPageLocators.CARD_NUMBER_INPUT_LOCATOR).send_keys(cc_number)
        self.driver.find_element(*CheckoutPageLocators.CARD_EXPIRATION_DATE_INPUT_LOCATOR).send_keys(date)
        self.driver.find_element(*CheckoutPageLocators.CARD_SECURITY_CODE_INPUT_LOCATOR).send_keys(cvv)
        self.driver.find_element(*CheckoutPageLocators.NAME_INPUT_LOCATOR).send_keys('John Doe')

    def click_on_place_order(self):
        self.driver.find_element(*CheckoutPageLocators.PLACE_ORDER_BUTTON_LOCATOR).click()

    def wait_for_thank_you_message_to_appear(self):
        WebDriverWait(self.driver, self.TIME_SEC).until(
            EC.presence_of_element_located(CheckoutPageLocators.THANK_YOU_MESSAGE_LOCATOR))
        WebDriverWait(self.driver, self.TIME_SEC).until(
            EC.presence_of_element_located(CheckoutPageLocators.PANEL_CONFIRMATION_EMAIL_LOCATOR))

    def the_finish_page_is_fully_loaded(self):
        checkout = CheckoutPage(self.driver)
        checkout.wait_for_thank_you_message_to_appear()
        thank_you_page = ThankYouPage(self.driver)
        thank_you_page.get_reference_number_from_finish_page()
