from django.conf  import settings

import hashlib
import base64
import json
import requests
from datetime import datetime
import calendar
import string
from random import *
import hmac

class Rapyd():
    RAPYD_SECRET_KEY = settings.RAPYD_SECRET_KEY  
    http_method = 'post'                   # get|put|post|delete - must be lowercase
    base_url = 'https://sandboxapi.rapyd.net'
    path = '/v1/checkout'           # Portion after the base URL. Hardkeyed for this example.

    def verify_payment(self, ref, *args, **kwargs):
        headers = {
            'access_key': access_key,
            'signature': signature,
            'salt': salt,
            'timestamp': str(timestamp),
            'Content-Type': "application\/json"
        }
        

    def get_redirect_url(products, price):

        # salt: randomly generated for each request.
        min_char = 8
        max_char = 12
        allchar = string.ascii_letters + string.punctuation + string.digits
        salt = "".join(choice(allchar)for x in range(randint(min_char, max_char)))

        # Current Unix time (seconds).
        d = datetime.utcnow()
        timestamp = calendar.timegm(d.utctimetuple())

        access_key = '23F7E00B653E2FE3DF3E' 
        secret_key = '9d45afe25456eebbb323e1249e946679cbab83e9d116fdc9a0fb6384a2d17f1fa07ed84c47532f2f'        # The access key received from Rapyd.
            # Never transmit the secret key by itself.

        checkout_body = {}
        checkout_body['amount'] = price
        checkout_body['country'] = 'US'
        checkout_body['currency'] = 'USD'
        checkout_body['complete_checkout_url'] = "127.0.0.1:8000/checkout"


        body = json.dumps(checkout_body, separators = (',',':'))
        
                                # JSON body goes here. Always empty string for GET; 
                                            # strip nonfunctional whitespace.

        to_sign = http_method + path + salt + str(timestamp) + access_key + secret_key + body

        h = hmac.new(bytes(secret_key, 'utf-8'), bytes(to_sign, 'utf-8'), hashlib.sha256)

        signature = base64.urlsafe_b64encode(str.encode(h.hexdigest()))

        url = base_url + path

        headers = {
            'access_key': access_key,
            'signature': signature,
            'salt': salt,
            'timestamp': str(timestamp),
            'Content-Type': "application\/json"
        }

        print(url)

        response = requests.post(url, headers = headers, json = checkout_body)
        hosted_checkout_url = response.json()['data']['redirect_url']

        
        return hosted_checkout_url
    #print(r.text)