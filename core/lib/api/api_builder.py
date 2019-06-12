from time import strftime
import hmac
import requests
import time
from core.lib.common import merchant
import json


class ApiBuilder:

    @staticmethod
    def set_auth_header(id_account, header_type):
        """
        This function calculates the auth header key and value for REST API.
        :param header_type: Select header type : API or CONVERT_PLUS
        :type header_type: str
        :type id_account: int - Vendor account id.
        :return array - contains Avangate authHeader key and value
        """
        vendor = merchant.Merchant()
        key = b'vendor.get_account_details(id_account, key_name="IpNKey")'
        merchant_code = vendor.get_account_details(id_account, key_name="ClientCode")
        date = strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        string = (str(len(merchant_code))+merchant_code+str(len(date))+date).encode()
        hash_key = hmac.new(key, string)
        if header_type is "API":
            header = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                'X-Avangate-Authentication': "code='" + merchant_code + "' date='" + date + "' hash='"
                                             + hash_key.hexdigest() + "'",
            }
            return header
        elif header_type is "CONVERT_PLUS":
            header = {
                "Content-Type": "application/json",
                'X-Avangate-Authentication': 'type="private" app="jscart" ver="1" '
                                             'hash="okA0htp1NARjq0irE37f2uOMnqwuH71subgn3AHjYrcncjxi2m2icCWHA4IO33nY"',
            }
            return header
        else:
            raise Exception("Please select header. The two options are 'API' or 'CONVERT_PLUS'.")

    def api_call(self, host_url, header_type, http_method, request_data, id_account=None):
        """
        This function initializes the REST service and authenticates in REST API.
        :param host_url: REST API url
        :type host_url: str
        :param header_type: Select header type : API or CONVERT_PLUS
        :type header_type: str
        :param http_method: Specific REST method (POST, GET, PUT, DELETE)
        :type http_method: str
        :param request_data: REST method payload
        :type request_data: dict
        :param id_account: Vendor id account
        :type id_account: int
        :return:
        :rtype: str
        """
        supported_http_methods = ["POST", "GET", "PUT", "DELETE"]
        if http_method not in supported_http_methods:
            raise ValueError(f"'{http_method}' method is not supported: Current supported methods: "
                             f"{supported_http_methods}")
        header = ApiBuilder.set_auth_header(id_account, header_type)

        if http_method is "POST":
            response = requests.post(host_url, data=json.dumps(request_data), headers=header)
        elif http_method is "GET":
            response = requests.get(host_url, data=json.dumps(request_data), headers=header)
        elif http_method is "PUT":
            response = requests.put(host_url, data=json.dumps(request_data), headers=header)
        elif http_method is "DELETE":
            response = requests.delete(host_url, data=json.dumps(request_data), headers=header)

        if (response.content and response.status_code) is None:
            raise Exception(f"Request to: {host_url}, action: {http_method} failed with error: {response.status_code}")
        else:
            response_string = response.content
            output_list = json.loads(response_string)
            return output_list[0]
