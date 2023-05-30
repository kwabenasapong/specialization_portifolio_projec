#!/usr/bin/env python3

'''
This is a test script to send a message using the MTN API
AppName = bulkSMSSender
'''

import requests

# get access token for MTN API
import requests

url = "https://api.mtn.com/v1/oauth/access_token?grant_type=client_credentials"
payload = "client_id=OtYI2bLjnInCpyW1K6keohVZRKKIsz1f&client_secret=Hd3bmuAjAm44Ddmx"
headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }

token_response = requests.request("POST", url, data=payload, headers=headers)

# get access token using get() method
token = token_response.json().get('access_token')

print(token_response.text)

print('token: ', token)
print('---------------------------------')

# send message using the access token
url = "https://api.mtn.com/v3/sms/messages/sms/outbound"

payload = {
    "senderAddress": "VALCO",
    "receiverAddress": ["233548257283", "233202419977"],
    "message": "Test message from VALCO",
    "clientCorrelatorId": "test123",
    "keyword": "string",
    "serviceCode": "1000",
    "requestDeliveryReceipt": False
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token
}
print(headers)

try:
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.status_code)
    message = response.json()
    print(response.text)
except:
    print("Message not sent")


""" url = "https://api.mtn.com/v2/messages/sms/outbound"

payload = {
    "senderAddress": "548257283",
    "receiverAddress": ["202419977"],
    "message": "string",
    "clientCorrelator": "string"
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {token}"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text) """

