import core

from core.modules.api.rest_client import RestClient
from core.modules.api.rpc_client import RpcClient


class Subscriptions:
    ACCOUNT_ID = 41764
    RECURRING_SUBSCRIPTION = "85419FDC8C"

    REST_CALL = None
    RPC_CALL = None

    def __init__(self, host):
        self.host = host.replace("http://", "http://api.")
        self.account_id = self.ACCOUNT_ID
        self.db_actor = core.get(core.res['mysql'], feature="dbaccess")

        self.REST_CALL = RestClient()
        self.RPC_CALL = RpcClient()

    def get_subscription_reference(self, sub_ref):
        subscription_reference = self.db_actor.get_subscription_reference(
            self.RECURRING_SUBSCRIPTION, key_name="LicenceCode")
        assert subscription_reference == sub_ref

