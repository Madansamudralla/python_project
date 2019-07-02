from features.convert_plus.locators.checkout_page import CheckoutPageLocators
import core


class ThankYouPage:
    TIME_SEC = 5

    def __init__(self):
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

    def get_reference_number_from_finish_page(self):
        elements = self.driver.find_elements(*CheckoutPageLocators.FINISH_PAGE_REFERENCE_NUMBER_LOCATOR)
        return elements[0].text
