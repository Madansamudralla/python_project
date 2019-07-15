import core

from core.modules.api_builder import ApiBuilder


class GetSubscription:
    CALL = None
    ACCOUNT_ID = 41764
    SUBSCRIPTION_REFERENCE = "85419FDC8C"

    def __init__(self, host):
        self.host = host.replace("http://", "http://api.")
        self.account_id = self.ACCOUNT_ID
        self.db_actor = core.get(core.res['mysql'], feature="dbaccess")
        self.merchant_code = self.db_actor.get_account_details(self.account_id, key_name="ClientCode")

        self.CALL = ApiBuilder()

    def get_subscription_reference(self, sub_ref):
        subscription_reference = self.db_actor.get_subscription_reference(
            self.SUBSCRIPTION_REFERENCE, key_name="LicenceCode")
        assert subscription_reference == sub_ref

    def call_get_subscription(self, protocol, version, resource):
        response = self.CALL.api_call(f"{self.host}/{protocol}/{version}/{resource}/{self.SUBSCRIPTION_REFERENCE}/",
                                      "API", "GET", merchant_code=self.merchant_code)
        return response
