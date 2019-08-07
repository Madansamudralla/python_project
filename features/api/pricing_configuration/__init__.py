import core

from core.modules.api.rest_client import RestClient
from core.modules.api.rpc_client import RpcClient


class PricingConfiguration:
    ACCOUNT_ID = 41764
    DIGITAL_PRODUCT = "p4p4na51"
    PRICING_CONFIGURATION_CODE = "5B20EF595F"
    REST_CALL = None
    RPC_CALL = None

    def __init__(self, host):
        self.host = host.replace("http://", "http://api.")
        self.account_id = self.ACCOUNT_ID
        self.db_actor = core.get(core.res['mysql'], feature="dbaccess")

        self.REST_CALL = RestClient()
        self.RPC_CALL = RpcClient()