import core

from core.modules.api_builder import ApiBuilder


class BuyLinkThroughApi:
    BUY_LINK = None

    REQUEST_DATA_DEFAULT = {
        "data": [
            {
                "hostData": {
                    "name": "sandbox86.avangate.local",
                    "protocol": "http:"
                },
                "buyLinkData": {
                    "merchant": "9897",
                    "products": [
                        {
                            "code": "p4p4na51"
                        }
                    ]
                }
            }
        ]
    }

    REQUEST_DATA_ONE_COLUMN = {
        "data": [
            {
                "hostData": {
                    "name": "sandbox86.avangate.local",
                    "protocol": "http:"
                },
                "buyLinkData": {
                    "merchant": "9897",
                    "tpl": "one-column",
                    "products": [
                        {
                            "code": "p4p4na51"
                        }
                    ]
                }
            }
        ]
    }

    def __init__(self, host, account_id):
        self.host = host
        self.account_id = account_id
        self.db_actor = core.get(core.res['mysql'], feature="dbaccess")
        self.merchant_code = self.db_actor.get_account_details(self.account_id, key_name="ClientCode")

        self.BUY_LINK = ApiBuilder()

    def buy_link_with_one_regular_product_on_default_template(self):
        buy_link_with_one_regular_product_on_default_template = self.BUY_LINK.api_call(
            f"{self.host}/checkout/api/encrypt/generate/buy",
            "CONVERT_PLUS", "POST", self.REQUEST_DATA_DEFAULT, self.merchant_code)
        return buy_link_with_one_regular_product_on_default_template["url"]

    def buy_link_with_one_regular_product_on_one_column_template(self):

        buy_link_with_one_regular_product_on_one_column_template = \
            self.BUY_LINK.api_call(
                f"{self.host}/checkout/api/encrypt/generate/buy",
                "CONVERT_PLUS", "POST", self.REQUEST_DATA_ONE_COLUMN, self.merchant_code)
        return buy_link_with_one_regular_product_on_one_column_template["url"]

    def get_on_base_url(self, template):
        if template == "default":
            url = self.buy_link_with_one_regular_product_on_default_template()
        elif template == "one-column":
            url = self.buy_link_with_one_regular_product_on_one_column_template()
        browser = core.get(core.res['chrome'], feature="browser")
        browser.get_address(url)
