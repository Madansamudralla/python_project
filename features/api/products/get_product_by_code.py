import core

from core.modules.api.rest_client import RestClient
from core.modules.api.rpc_client import RpcClient


class GetProductByCode:
    REST_CALL = None
    RPC_CALL = None
    ACCOUNT_ID = 41764
    DIGITAL_PRODUCT = "p4p4na51"

    def __init__(self, host):
        self.host = host.replace("http://", "http://api.")
        self.account_id = self.ACCOUNT_ID
        self.db_actor = core.get(core.res['mysql'], feature="dbaccess")

        self.REST_CALL = RestClient()
        self.RPC_CALL = RpcClient()

    def see_product_status(self, status):
        db_status = self.db_actor.get_product_status(self.account_id, self.DIGITAL_PRODUCT, key_name="ProductStatus")
        assert db_status.lower() == status
        return status

    def get_product_by_code_rest(self, version, resource):
        response = self.REST_CALL.api_call(f"{self.host}/rest/{version}/{resource}/{self.DIGITAL_PRODUCT}/", "GET")
        return response

    def get_product_by_code_rpc(self, version):
        response = self.RPC_CALL.api_call("getProductByCode", f"{self.host}/rpc/{version}/", self.DIGITAL_PRODUCT)
        return response
