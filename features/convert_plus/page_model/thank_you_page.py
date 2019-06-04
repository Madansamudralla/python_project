from features.convert_plus.locators.checkout_page import CheckoutPageLocators


class ThankYouPage:
    TIME_SEC = 30

    def __init__(self, driver):
        self.driver = driver

    def get_reference_number_from_finish_page(self):
        elements = self.driver.find_elements(*CheckoutPageLocators.FINISH_PAGE_REFERENCE_NUMBER_LOCATOR)
        return elements[0].text
