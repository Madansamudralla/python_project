from behave import *
from selenium import webdriver


# class Environment:
#     CHROME_OPTIONS = None
#
#     def __init__(self):
#         self.CHROME_OPTIONS = webdriver.ChromeOptions()
#         self.CHROME_OPTIONS.accept_untrusted_certs = True
#         self.CHROME_OPTIONS.assume_untrusted_cert_issuer = True
#         self.CHROME_OPTIONS.add_argument("--no-sandbox")
#         self.CHROME_OPTIONS.add_argument("--disable-impl-side-painting")
#         self.CHROME_OPTIONS.add_argument("--disable-setuid-sandbox")
#         self.CHROME_OPTIONS.add_argument("--disable-seccomp-filter-sandbox")
#         self.CHROME_OPTIONS.add_argument("--disable-breakpad")
#         self.CHROME_OPTIONS.add_argument("--disable-client-side-phishing-detection")
#         self.CHROME_OPTIONS.add_argument("--disable-cast")
#         self.CHROME_OPTIONS.add_argument("--disable-cast-streaming-hw-encoding")
#         self.CHROME_OPTIONS.add_argument("--disable-cloud-import")
#         self.CHROME_OPTIONS.add_argument("--disable-popup-blocking")
#         self.CHROME_OPTIONS.add_argument("--ignore-certificate-errors")
#         self.CHROME_OPTIONS.add_argument("--disable-session-crashed-bubble")
#         self.CHROME_OPTIONS.add_argument("--disable-ipv6")
#         self.CHROME_OPTIONS.add_argument("--allow-http-screen-capture")
#         self.CHROME_OPTIONS.add_argument("--start-maximized")

    # @staticmethod
def before_scenario(context, scenario):
    # options = self.CHROME_OPTIONS
    # context.driver = webdriver.Chrome('.\chromedriver', chrome_options=options)
    # context.driver = webdriver.Chrome()
    # yield
    # context.driver.quit()
    context.driver = browser_set_up("chrome")

def browser_set_up(browser):
    if browser == "chrome":
        driver = webdriver.Chrome("http://localhost:4444/wd/hub")
        driver.maximize_window()
        return driver
