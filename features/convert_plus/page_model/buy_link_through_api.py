from core.lib.api.api_builder import ApiBuilder
from core.lib.browser.browser import Browser


class BuyLinkThroughApi:
    BUY_LINK = None
    URL = None
    ID_ACCOUNT = 41764
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

    def __init__(self):
        self.BUY_LINK = ApiBuilder()

    def buy_link_with_one_regular_product_on_default_template(self):
        buy_link_with_one_regular_product_on_default_template = self.BUY_LINK.api_call("http://sandbox86.avangate.local"
                                                      "/checkout/api/encrypt/generate/buy",
                                                      "CONVERT_PLUS", "POST", self.REQUEST_DATA_DEFAULT, self.ID_ACCOUNT)
        return buy_link_with_one_regular_product_on_default_template["url"]

    def buy_link_with_one_regular_product_on_one_column_template(self):
        buy_link_with_one_regular_product_on_one_column_template = \
            self.BUY_LINK.api_call("http://sandbox86.avangate.local/checkout/api/encrypt/generate/buy",
                                   "CONVERT_PLUS", "POST", self.REQUEST_DATA_ONE_COLUMN, self.ID_ACCOUNT)
        return buy_link_with_one_regular_product_on_one_column_template["url"]

    def get_on_base_url(self, template):
        if template == "default":
            self.URL = self.buy_link_with_one_regular_product_on_default_template()
        elif template == "one-column":
            self.URL = self.buy_link_with_one_regular_product_on_one_column_template()
        Browser.get_instance().driver.get(self.URL)
