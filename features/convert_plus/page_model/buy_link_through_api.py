from core.lib.api.api_builder import ApiBuilder
import core


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
        self.BUY_LINK = ApiBuilder()

    def buy_link_with_one_regular_product_on_default_template(self):
        buy_link_with_one_regular_product_on_default_template = self.BUY_LINK.api_call(
            f"{self.host}/checkout/api/encrypt/generate/buy",
                                                      "CONVERT_PLUS", "POST", self.REQUEST_DATA_DEFAULT, self.account_id)
        return buy_link_with_one_regular_product_on_default_template["url"]

    def buy_link_with_one_regular_product_on_one_column_template(self):
        buy_link_with_one_regular_product_on_one_column_template = \
            self.BUY_LINK.api_call(
                f"{self.host}/checkout/api/encrypt/generate/buy",
                                   "CONVERT_PLUS", "POST", self.REQUEST_DATA_ONE_COLUMN, self.account_id)
        return buy_link_with_one_regular_product_on_one_column_template["url"]

    def get_on_base_url(self, template):
        if template == "default":
            url = self.buy_link_with_one_regular_product_on_default_template()
        elif template == "one-column":
            url = self.buy_link_with_one_regular_product_on_one_column_template()
        browser = core.get({'host': 'localhost', 'port': 4444}, delegator="chrome")
        browser.driver.get(url)
