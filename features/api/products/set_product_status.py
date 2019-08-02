from features.api.products import Products


class SetProductStatus(Products):

    def __init__(self, host):
        super().__init__(host)

    def set_product_status_disabled_rest(self, version, resource, product_code):
        response = self.REST_CALL.api_call(f"{self.host}/rest/{version}/{resource}/{product_code}/", "DELETE")
        return response

    def set_product_status_enabled_rest(self, version, resource, product_code):
        response = self.REST_CALL.api_call(f"{self.host}/rest/{version}/{resource}/{product_code}/", "POST")
        return response

    def set_product_status_rpc(self, version, product_code, status):
        response = self.RPC_CALL.api_call("setProductStatus", f"{self.host}/rpc/{version}/", [product_code, status])
        return response
