from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    url = None

    def __init__(self, driver, url):
        self.driver = driver
        self.timeout = 30
        self.url = url
        self.implicit_wait = 15

    def fill_form_by_name(self, form_css, value):
        return self.driver.find_element_by_name(form_css).send_keys(value)
        # elem.send_keys(value)

    def fill_form_by_id(self, form_element_id, value):
        return self.driver.find_element_by_id(form_element_id).send_keys(value)

    def navigate(self):
        self.driver.get(self.url)

    def wait_till_specific_element_is_not_displayed(self, element):
        try:
            wait = WebDriverWait(self.driver, self.implicit_wait)
            expected_element = EC.visibility_of_element_located(element)
            wait.until(expected_element)
            return True
        except TimeoutError:
            raise

    def click_on_element_by_id(self, element):
        self.driver.find_element_by_id(element).click()
