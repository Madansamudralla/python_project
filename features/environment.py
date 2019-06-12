import core
import time
from core import DEFAULT_CONFIG_PATH, load_custom_config
CURRENT_CONFIG = {}


def before_all(context):
    global CURRENT_CONFIG
    config_file = context.config.userdata.get('profile', DEFAULT_CONFIG_PATH)
    if config_file != DEFAULT_CONFIG_PATH:
        config_file += "_config.yaml"
    CURRENT_CONFIG = load_custom_config(config_file)


def before_scenario(context, scenario):
    context.configuration = CURRENT_CONFIG
    resource = {"host": context.configuration['selenium']['host'],
                "port":  context.configuration['selenium']['port']
                }
    context.browser = core.get(resource, delegator="chrome")


def after_scenario(context, scenario):
    resource = {"host": context.configuration['selenium']['host'],
                "port": context.configuration['selenium']['port']
                }
    if scenario.status == "failed":
        browser = core.get(resource, delegator="chrome")
        browser.driver.save_screenshot(
            f"{context.configuration['screenshots']}/{scenario.name}_{time.strftime('%d-%m-%Y_%H-%M-%S')}.png")

    core.remove(resource, delegator="chrome")

