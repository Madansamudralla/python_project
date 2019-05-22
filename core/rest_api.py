from time import strftime
import hmac
import requests
import time
import json


url = "http://api.sandbox76.avangate.local/rest/6.0/products/blablabla/" #TODO get URL from url builder


class RestApi:

    def auth_header(idaccount):
        #TODO implement vendor data/factory
        #vendor = #get all details of vendor by idAccount
        # key = vendor["IpnKey"]
        # merchantCode = vendor["ClientCode"]
        key = b"n%T1?8@6|z2+8a62FK28"
        merchant_code = "120000869760"
        date = strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        string = (str(len(merchant_code))+merchant_code+str(len(date))+date).encode()
        hash_key = hmac.new(key, string)
        header = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            'X-Avangate-Authentication': "code='"+merchant_code+"' date='"+date+"' hash='"+hash_key.hexdigest()+"'",
        }

        return header

    def call_rest(idaccount=None, method=None, callurl=None, request_data=None):
        response = requests.request(method, callurl, data=request_data, headers=RestApi.auth_header(idaccount))
        print(response.text)


