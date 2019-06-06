from selenium import webdriver
import config_automation


class Browser(object):

    HOST = "http://" + config_automation.Config.SELENIUM_HOST + ":" \
           + str(config_automation.Config.SELENIUM_PORT) + "/wd/hub"

    CAPS = {
        "browserName": 'chrome'
    }

    INSTANCE = None

    def __init__(self):
        self.driver = webdriver.Remote(self.HOST, self.CAPS)
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        self.driver.maximize_window()

    @classmethod
    def get_instance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = cls()

        return cls.INSTANCE

    def close(self):
        self.driver.quit()
        Browser.INSTANCE = None
