from core.Basepage import BasePage
import time
import conf


class LoginPage(BasePage):
    def __init__(self, driver):
        self.url = conf.Url
        BasePage.__init__(self, driver, self.url)

    def fill_xpath(self):
        time.sleep(4)
        super.driver.find_element_by_xpath("//*[text()='SignIn']").click()
        time.sleep(5)

    def setUserName(self, user):
        BasePage.fill_form_by_id(self, "username", user)

    def setPassword(self, password):
        BasePage.fill_form_by_id(self, "password", password)

    def submit(self):
        BasePage.click_on_element_by_id(self, 'Login')
        time.sleep(4)
