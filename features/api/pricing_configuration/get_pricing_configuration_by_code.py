from core.modules.api.rest_client import RestClient
from core.modules.api.rpc_client import RpcClient
from features.api.pricing_configuration import PricingConfiguration


class GetPricingConfigurationByCode(PricingConfiguration):
    ACCOUNT_ID = 41764
    DIGITAL_PRODUCT = "p4p4na51"
    PRICING_CONFIGURATION_CODE = "5B20EF595F"
    REST_CALL = None
    RPC_CALL = None

    def __init__(self, host):
        super().__init__(host)

        self.REST_CALL = RestClient()
        self.RPC_CALL = RpcClient()

    def get_pricing_configuration_by_code_rest(self, version, resource, product_code, pricing_configuration_code):
        response = self.REST_CALL.api_call(
            f"{self.host}/rest/{version}/{resource}/{product_code}/pricingconfigurations/{pricing_configuration_code}/",
            "GET"
        )
        return response

    def get_pricing_configuration_by_code_rpc(self, version, product_code, pc_code):
        response = self.RPC_CALL.api_call(
            "getPricingConfigurationByCode", f"{self.host}/rpc/{version}/", [product_code, pc_code]
        )
        return response


