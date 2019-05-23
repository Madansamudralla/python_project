from selenium import webdriver
import config_automation

HOST = "http://" + config_automation.Config.SELENIUM_HOST + ":" \
       + str(config_automation.Config.SELENIUM_PORT) + "/wd/hub"

# TODO - research for HOST variable usage in old framework
# TODO - research how to run steps from different path steps directory


def before_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser = webdriver.Chrome()
        context.browser.maximize_window()
        # context.browser.get(url=HOST)
        context.browser.set_page_load_timeout(30)


def after_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser.quit()
