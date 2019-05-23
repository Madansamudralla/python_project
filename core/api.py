from time import strftime
import hmac
import requests
import time
from core import merchant


class Api:

    def auth_header(self, id_account):
        """
        This function calculates the auth header key and value for REST API.
        :type id_account: int - Vendor account id.
        :return array - contains Avangate authHeader key and value
        """
        vendor = merchant.Merchant()
        key = b'vendor.get_ipn_key(id_account)'
        merchant_code = vendor.get_client_code(id_account)
        date = strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        string = (str(len(merchant_code))+merchant_code+str(len(date))+date).encode()
        hash_key = hmac.new(key, string)
        header = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            'X-Avangate-Authentication': "code='" + merchant_code + "' date='" + date + "' hash='"
                                         + hash_key.hexdigest() + "'",
        }
        return header

    def call_rest(self, id_account=None, method=None, host_url=None, request_data=None):
        """
        This function is using auth_header() to send REST requests
        :type id_account: int - Vendor account id for auth_header.
        :type method: str - REST method for request(GET,POST,DELETE,PUT)
        :type host_url: str - End point URL
        :type request_data: json - Body for POST/PUT methods

        :return response: dict - contains the response of the REST request
        """
        response = requests.request(method, host_url, data=request_data, headers=Api.auth_header(self, id_account))
        if response is None:
            raise Exception("No response received.")
        else:
            return response
