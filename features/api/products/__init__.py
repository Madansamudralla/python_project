import core

from core.modules.api.rest_client import RestClient
from core.modules.api.rpc_client import RpcClient


class Products:
    ACCOUNT_ID = 41764
    DIGITAL_PRODUCT = "p4p4na51"
    DISABLED_DIGITAL_PRODUCT = "DISABLED_DIGITAL"
    ENABLED_DIGITAL_PRODUCT = "ENABLED_DIGITAL"
    DISABLED_PHYSICAL_PRODUCT = "DISABLED_PHYSICAL"
    ENABLED_PHYSICAL_PRODUCT = "ENABLED_PHYSICAL"
    REST_CALL = None
    RPC_CALL = None

    def __init__(self, host):
        self.host = host.replace("http://", "http://api.")
        self.account_id = self.ACCOUNT_ID
        self.db_actor = core.get(core.res['mysql'], feature="dbaccess")

        self.REST_CALL = RestClient()
        self.RPC_CALL = RpcClient()

    def get_product_status_db(self, product_code, status):
        db_status = self.db_actor.get_product_status(self.account_id, product_code, key_name="ProductStatus")
        assert db_status.lower() == status, f"Expected: {status} Actual: {db_status.lower()}"
        return status

    def set_product_status_db(self, product_code, status):
        self.db_actor.set_product_status(self.account_id, product_code, status.upper())
        db_get_status = self.db_actor.get_product_status(self.account_id, product_code, key_name="ProductStatus")
        assert db_get_status.lower() == status
