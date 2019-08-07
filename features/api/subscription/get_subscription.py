from features.api.subscription import Subscriptions


class GetSubscription(Subscriptions):
    REST_CALL = None
    RPC_CALL = None
    ACCOUNT_ID = 41764

    def __init__(self, host):
        super().__init__(host)

    def call_get_subscription_rest(self, version, resource):
        response = self.REST_CALL.api_call(
            f"{self.host}/rest/{version}/{resource}/{self.RECURRING_SUBSCRIPTION}/", "GET"
        )
        return response

    def call_get_subscription_rpc(self, version):
        response = self.RPC_CALL.api_call(
            "getSubscription", f"{self.host}/rpc/{version}/", [self.RECURRING_SUBSCRIPTION]
        )
        return response
