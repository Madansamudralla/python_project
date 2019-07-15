from time import strftime
import hmac
import requests
import time
import hashlib

import json

import core


class ApiBuilder:

    @staticmethod
    def set_x_avangate_auth_header(merchant_code, header_type):
        """Method to create X-Avangate-Authentication headers.

            args:
                :header_type (str): The API version to be used for testing. API(Default)|CONVERT_PLUS.
                :merchant_code (int): Vendor ID account.

            returns:
                An array contains X-Avangate-Authentication headers value.
        """
        account_id = 41764
        db_actor = core.get(core.res['mysql'], feature="dbaccess")
        key = db_actor.get_account_details(account_id, key_name="IpnKey").encode()

        date = strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        string = (str(len(merchant_code))+merchant_code+str(len(date))+date).encode()
        hash_key = hmac.new(key, string, hashlib.md5)
        if header_type is "API":
            header = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                'X-Avangate-Authentication': f'code="{merchant_code}" date="{date}" hash="{hash_key.hexdigest()}"',

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

    def api_call(self, host_url, header_type, http_method, request_data=None, merchant_code=None):

        timeout = 30

        """Method to create X-Avangate-Authentication headers.

            args:
                :host_url (str): API url endpoint.
                :header_type (str): The API version to be used for testing. API(Default)|CONVERT_PLUS.
                :http_method (str): The http method that it is used for the request (POST, GET, PUT, DELETE)
                :request_data (dict): Dictionary where user can specify the entire body of the request.
                :merchant_code (int): Vendor ID account.

            returns:
                An array contains X-Avangate-Authentication headers value.
        """
        supported_http_methods = ["POST", "GET", "PUT", "DELETE"]
        if http_method not in supported_http_methods:
            raise ValueError(f"'{http_method}' method is not supported: Current supported methods: "
                             f"{supported_http_methods}")
        header = ApiBuilder.set_x_avangate_auth_header(merchant_code, header_type)

        if http_method is "POST":
            response = requests.post(host_url, data=json.dumps(request_data), headers=header)
        elif http_method is "GET":
            response = requests.get(host_url, headers=header, timeout=timeout)
        elif http_method is "PUT":
            response = requests.put(host_url, data=json.dumps(request_data), headers=header)
        elif http_method is "DELETE":
            response = requests.delete(host_url, data=json.dumps(request_data), headers=header)

        if (response.content and response.status_code) is None:
            raise Exception(f"Request to: {host_url}, action: {http_method} failed with error: {response.status_code}")
        else:
            return response
            # response_string = response.content
            # output_list = json.loads(response_string)
            # return output_list
