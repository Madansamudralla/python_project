from selenium import webdriver
import config_automation
import time


HOST = "http://" + config_automation.Config.SELENIUM_HOST + ":" \
       + str(config_automation.Config.SELENIUM_PORT) + "/wd/hub"

# TODO - research for HOST variable usage in old framework
# TODO - research how to run steps from different path steps directory


"""
Initialize browser handle or selenium webdriver handle based on the choice of browser
Command "behave -D BROWSER=chrome"
"""


def before_scenario(context, scenario):
    print("\nRunning scenarios with this user data: ", context.config.userdata)

    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            BROWSER = 'chrome'
        else:
            BROWSER = context.config.userdata['BROWSER']
    else:
        BROWSER = 'chrome'

    if BROWSER == 'chrome':
        context.browser = webdriver.Chrome('./chromedriver')
    elif BROWSER == 'firefox':
        context.browser = webdriver.Firefox()
    elif BROWSER == 'safari':
        context.browser = webdriver.Safari()
    elif BROWSER == 'ie':
        context.browser = webdriver.Ie()
    else:
        print("Browser you entered:", BROWSER, "is invalid value")

    context.browser.maximize_window()
    context.browser.set_page_load_timeout(30)
    print("Start running scenario: " + scenario.name + "\n")


"""
Dump all screenshots in specific folder and quit webdriver to use a fresh webdriver session for every scenario.
"""


def after_scenario(context, scenario):
    if scenario.status == "failed":
        context.browser.save_screenshot(config_automation.Config.SCREENSHOTPATH + "/" +
                                        scenario.name + "_" + time.strftime("%d-%m-%Y_%H-%M-%S") + ".png")
    context.browser.close()
    context.browser.quit()

