import os
import yaml

from core.lib.browser.browser_manager import BrowserManager
browser_manager = BrowserManager()
DEFAULT_CONFIG_PATH = "default_config.yaml"


def load_custom_config(config_path):
    default_config = load_yaml(DEFAULT_CONFIG_PATH)
    custom_config = load_yaml(config_path)
    default_config.update(custom_config)

    if not os.path.exists(default_config['screenshots']):
        os.makedirs(default_config['screenshots'], 0o775)
    return default_config


def load_yaml(yaml_file=DEFAULT_CONFIG_PATH):
    with open(yaml_file) as f:
        content = yaml.safe_load(f)
    return content


def get(resource, delegator):
    if delegator == "chrome":
        from core.lib.browser.chrome import Chrome
    elif delegator == "firefox":
        from core.lib.browser.firefox import Firefox
    host = resource['host']
    port = resource['port']
    actor = browser_manager.get(Chrome, host, port)
    return actor


def remove(resource, delegator):
    if delegator == "chrome":
        from core.lib.browser.chrome import Chrome
    elif delegator == "firefox":
        from core.lib.browser.firefox import Firefox
    host = resource['host']
    port = resource['port']
    actor = browser_manager.remove(Chrome, host, port)
    return actor
