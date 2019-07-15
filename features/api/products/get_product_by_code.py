import core

from core.modules.api_builder import ApiBuilder


class GetProductByCode:
    CALL = None
    ACCOUNT_ID = 41764
    DIGITAL_PRODUCT = "p4p4na51"

    def __init__(self, host):
        self.host = host.replace("http://", "http://api.")
        self.account_id = self.ACCOUNT_ID
        self.db_actor = core.get(core.res['mysql'], feature="dbaccess")
        self.merchant_code = self.db_actor.get_account_details(self.account_id, key_name="ClientCode")

        self.CALL = ApiBuilder()

    def see_product_status(self, status):
        db_status = self.db_actor.get_product_status(self.account_id, self.DIGITAL_PRODUCT, key_name="ProductStatus")
        assert db_status.lower() == status
        return status

    def call_get_product_by_code(self, protocol, version, resource):
        response = self.CALL.api_call(f"{self.host}/{protocol}/{version}/{resource}/{self.DIGITAL_PRODUCT}/",
                                      "API", "GET", merchant_code=self.merchant_code)
        return response
