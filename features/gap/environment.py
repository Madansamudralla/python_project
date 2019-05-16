from selenium import webdriver
import paramiko
import conf


def before_feature(context, scenario):
    context.driver = browser_set_up("chrome")
    print(context.driver)


# def before_tag(context, tag):
#     if tag.find("browser"):
#         context.driver = browser_set_up(context, "chrome")
#         print(context.driver)
#     elif tag.find("cron"):
#         context.client = cron_set_up(context)


def browser_set_up(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(conf.Chrome)
        driver.maximize_window()
        return driver

def cron_set_up():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(conf.CRON_HOST, 22, conf.USER, conf.key)
    return client

# def web_set_up(self, browser):
#     if browser == "chrome":
#         driver = webdriver.Chrome(conf.Chrome)
#         return driver
#
# def cron_setup(self):
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(conf.CRON_HOST, 22, conf.USER, conf.key)
#     return client
