import core
import os
import yaml
import json

from core.modules.api_builder import ApiBuilder

PROJECT_PATH = os.path.dirname(__file__)
FILE_NAME = "place_order.yaml"
FULL_REQUEST_PATH = os.path.join(PROJECT_PATH, FILE_NAME)

CURRENT_CONFIG = {}


class BuyLinkThroughApi:
    BUY_LINK = None
    ACCOUNT_ID = 41764
    # MERCHANT = 9897
    DIGITAL_PRODUCT = "p4p4na51"
    PHYSICAL_PRODUCT = "physical_product"

    def __init__(self, host):
        self.host = host
        self.account_id = self.ACCOUNT_ID
        self.db_actor = core.get(core.res['mysql'], feature="dbaccess")
        self.merchant_code = self.db_actor.get_account_details(self.account_id, key_name="ClientCode")

        self.BUY_LINK = ApiBuilder()
        # self.merchant = self.MERCHANT
        self.digital_product_code = self.DIGITAL_PRODUCT
        self.physical_product_code = self.PHYSICAL_PRODUCT

    def load_request(self, yaml_file=FULL_REQUEST_PATH):
        with open(yaml_file) as f:
            content = yaml.safe_load(f)
        return content

    def buy_link_with_one_digital_product_on_default_template(self):

        global CURRENT_CONFIG
        tpl = "default"

        CURRENT_CONFIG = self.load_request()
        CURRENT_CONFIG['data'][0]['buyLinkData']['merchant'] = self.merchant_code
        CURRENT_CONFIG['data'][0]['buyLinkData']['tpl'] = tpl
        CURRENT_CONFIG['data'][0]['buyLinkData']['products'][0]['code'] = self.digital_product_code
        CURRENT_CONFIG['data'][0]['hostData']['name'] = self.host.replace("http://", "")

        buy_link_with_one_regular_product_on_default_template = self.BUY_LINK.api_call(
            f"{self.host}/checkout/api/encrypt/generate/buy",
            "CONVERT_PLUS", "POST", CURRENT_CONFIG, self.merchant_code)

        response = json.loads(buy_link_with_one_regular_product_on_default_template.content)
        return response[0]["url"]

    def buy_link_with_one_digital_product_on_one_column_template(self):

        global CURRENT_CONFIG
        tpl = "one-column"

        CURRENT_CONFIG = self.load_request()
        CURRENT_CONFIG['data'][0]['buyLinkData']['merchant'] = self.merchant_code
        CURRENT_CONFIG['data'][0]['buyLinkData']['tpl'] = tpl
        CURRENT_CONFIG['data'][0]['buyLinkData']['products'][0]['code'] = self.digital_product_code
        CURRENT_CONFIG['data'][0]['hostData']['name'] = self.host.replace("http://", "")

        buy_link_with_one_regular_product_on_one_column_template = \
            self.BUY_LINK.api_call(
                f"{self.host}/checkout/api/encrypt/generate/buy",
                "CONVERT_PLUS", "POST", CURRENT_CONFIG, self.merchant_code)

        response = json.loads(buy_link_with_one_regular_product_on_one_column_template.content)
        return response[0]["url"]

    def get_on_base_url_catalog_digital_product(self, template):
        if template == "default":
            url = self.buy_link_with_one_digital_product_on_default_template()
        elif template == "one-column":
            url = self.buy_link_with_one_digital_product_on_one_column_template()
        browser = core.get(core.res['chrome'], feature="browser")
        browser.get_address(url)

    def buy_link_with_one_physical_product_on_default_template(self):

        global CURRENT_CONFIG
        tpl = "default"

        CURRENT_CONFIG = self.load_request()
        CURRENT_CONFIG['data'][0]['buyLinkData']['merchant'] = self.merchant_code
        CURRENT_CONFIG['data'][0]['buyLinkData']['tpl'] = tpl
        CURRENT_CONFIG['data'][0]['buyLinkData']['products'][0]['code'] = self.physical_product_code
        CURRENT_CONFIG['data'][0]['hostData']['name'] = self.host.replace("http://", "")

        buy_link_with_one_regular_product_on_default_template = self.BUY_LINK.api_call(
            f"{self.host}/checkout/api/encrypt/generate/buy",
            "CONVERT_PLUS", "POST", CURRENT_CONFIG, self.merchant_code)

        response = json.loads(buy_link_with_one_regular_product_on_default_template.content)
        return response[0]["url"]

    def buy_link_with_one_physical_product_on_one_column_template(self):

        global CURRENT_CONFIG
        tpl = "default"

        CURRENT_CONFIG = self.load_request()
        CURRENT_CONFIG['data'][0]['buyLinkData']['merchant'] = self.merchant_code
        CURRENT_CONFIG['data'][0]['buyLinkData']['tpl'] = tpl
        CURRENT_CONFIG['data'][0]['buyLinkData']['products'][0]['code'] = self.physical_product_code
        CURRENT_CONFIG['data'][0]['hostData']['name'] = self.host.replace("http://", "")

        buy_link_with_one_regular_product_on_default_template = self.BUY_LINK.api_call(
            f"{self.host}/checkout/api/encrypt/generate/buy",
            "CONVERT_PLUS", "POST", CURRENT_CONFIG, self.merchant_code)

        response = json.loads(buy_link_with_one_regular_product_on_default_template.content)
        return response[0]["url"]

    def get_on_base_url_catalog_physical_product(self, template):
        if template == "default":
            url = self.buy_link_with_one_physical_product_on_default_template()
        elif template == "one-column":
            url = self.buy_link_with_one_physical_product_on_one_column_template()
        browser = core.get(core.res['chrome'], feature="browser")
        browser.get_address(url)
