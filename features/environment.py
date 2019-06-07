from core.lib.browser.browser import Browser
import config_automation
import time


"""
Initialize browser handle or selenium webdriver handle based on the choice of browser
Command "behave -D BROWSER=chrome"
"""


# def before_scenario(context, scenario):
#     print("\nRunning scenarios with this user data: ", context.config.userdata)
#
#     if 'BROWSER' in context.config.userdata.keys():
#         if context.config.userdata['BROWSER'] is None:
#             BROWSER = 'chrome'
#         else:
#             BROWSER = context.config.userdata['BROWSER']
#     else:
#         BROWSER = 'chrome'
#
#     if BROWSER == 'chrome':
#         context.browser = webdriver.Chrome('./chromedriver')
#     elif BROWSER == 'firefox':
#         context.browser = webdriver.Firefox()
#     elif BROWSER == 'safari':
#         context.browser = webdriver.Safari()
#     elif BROWSER == 'ie':
#         context.browser = webdriver.Ie()
#     else:
#         print("Browser you entered:", BROWSER, "is invalid value")
#
#     context.browser.maximize_window()
#     context.browser.set_page_load_timeout(30)
#     print("Start running scenario: " + scenario.name + "\n")

def before_scenario(context, scenario):
    context.browser = Browser.get_instance()

"""
Dump all screenshots in specific folder and quit webdriver to use a fresh webdriver session for every scenario.
"""


def after_scenario(context, scenario):
    if scenario.status == "failed":
        Browser.get_instance().driver.save_screenshot(
            config_automation.Config.SCREENSHOTPATH + "/" + scenario.name + "_" + time.strftime(
                "%d-%m-%Y_%H-%M-%S") + ".png")
    context.browser.close()

