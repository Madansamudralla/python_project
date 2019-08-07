from features.api.products import Products


class GetProductByCode(Products):

    def __init__(self, host):
        super().__init__(host)

    def get_product_by_code_rest(self, version, resource):
        response = self.REST_CALL.api_call(f"{self.host}/rest/{version}/{resource}/{self.DIGITAL_PRODUCT}/", "GET")
        return response

    def get_product_by_code_rpc(self, version):
        response = self.RPC_CALL.api_call("getProductByCode", f"{self.host}/rpc/{version}/", [self.DIGITAL_PRODUCT])
        return response
