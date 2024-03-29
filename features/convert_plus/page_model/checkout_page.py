from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.convert_plus.locators.checkout_page import CheckoutPageLocators
from selenium.webdriver.common.keys import Keys
from features.convert_plus.page_model.thank_you_page import ThankYouPage
import core


class CheckoutPage:
    TIME_SEC = 5

    def __init__(self):
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

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

    def fill_name(self, name):
        self.driver.find_element(*CheckoutPageLocators.NAME_INPUT_LOCATOR).send_keys(name)

    def fill_direct_debit_details(self, name, iban, swift_code):
        self.fill_name(name)
        self.driver.find_element(*CheckoutPageLocators.IBAN_INPUT_LOCATOR).send_keys(iban)
        self.driver.find_element(*CheckoutPageLocators.SWIFT_CODE_INPUT_LOCATOR).send_keys(swift_code)

    def fill_wire_transfer_details(self, name):
        self.fill_name(name)

    def click_on_place_order(self):
        self.driver.find_element(*CheckoutPageLocators.PLACE_ORDER_BUTTON_LOCATOR).click()

    def fill_billing_details(self, country, email, catalog_product_type, address=None, city=None, zip=None, phone=None):
        self.fill_country(country)
        self.wait_for_loader_to_disappear()
        self.fill_email_address(email)
        if catalog_product_type == 'physical':
            self.driver.find_element(*CheckoutPageLocators.ADDRESS_INPUT_LOCATOR).send_keys(address)
            self.driver.find_element(*CheckoutPageLocators.CITY_INPUT_LOCATOR).send_keys(city)
            self.driver.find_element(*CheckoutPageLocators.ZIP_INPUT_LOCATOR).send_keys(zip)
            self.driver.find_element(*CheckoutPageLocators.PHONE_INPUT_LOCATOR).send_keys(phone)

    def select_direct_debit_as_a_payment_method(self):
        self.driver.find_element(*CheckoutPageLocators.OTHER_BUTTON).click()
        WebDriverWait(self.driver, self.TIME_SEC).until(
            EC.presence_of_element_located(CheckoutPageLocators.PAYMENT_METHOD_DIRECT_DEBIT_LOCATOR))
        self.driver.find_element(*CheckoutPageLocators.PAYMENT_METHOD_DIRECT_DEBIT_LOCATOR).click()

    def select_wire_transfer_as_a_payment_method(self):
        self.driver.find_element(*CheckoutPageLocators.OTHER_BUTTON).click()
        WebDriverWait(self.driver, self.TIME_SEC).until(
            EC.presence_of_element_located(CheckoutPageLocators.PAYMENT_METHOD_WIRE_TRANSFER_LOCATOR))
        self.driver.find_element(*CheckoutPageLocators.PAYMENT_METHOD_WIRE_TRANSFER_LOCATOR).click()

    def select_paypal_as_a_payment_method(self):
        self.driver.find_element(*CheckoutPageLocators.OTHER_BUTTON).click()
        WebDriverWait(self.driver, self.TIME_SEC).until(
            EC.presence_of_element_located(CheckoutPageLocators.PAYMENT_METHOD_PAYPAL_LOCATOR))
        self.driver.find_element(*CheckoutPageLocators.PAYMENT_METHOD_PAYPAL_LOCATOR).click()

    def wait_for_thank_you_message_to_appear(self):
        WebDriverWait(self.driver, self.TIME_SEC).until(
            EC.presence_of_element_located(CheckoutPageLocators.THANK_YOU_MESSAGE_LOCATOR))
        WebDriverWait(self.driver, self.TIME_SEC).until(
            EC.presence_of_element_located(CheckoutPageLocators.PANEL_CONFIRMATION_EMAIL_LOCATOR))

    @staticmethod
    def the_finish_page_is_fully_loaded():
        checkout = CheckoutPage()
        checkout.wait_for_thank_you_message_to_appear()
        thank_you_page = ThankYouPage()
        thank_you_page.get_reference_number_from_finish_page()

    def wait_for_checkout_page_to_load(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(CheckoutPageLocators.PLACE_ORDER_BUTTON_LOCATOR)
        )
