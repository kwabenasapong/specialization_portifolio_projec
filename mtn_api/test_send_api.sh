#!/usr/bin/bash

# Send SMS with MTN API
curl --request POST \
  --url https://api.mtn.com/v3/sms/messages/sms/outbound \
  --header 'Authorization: Bearer elFAyh7EmRysFZpVAHAnvl6N6tqh' \
  --header 'Content-Type: application/json' \
  --data '{
  "senderAddress": "VALCO",
  "receiverAddress": [
    "233548257283",
    "233202419977"
  ],
  "message": "api test works",
  "clientCorrelatorId": "00-test-api",
  "keyword": "string",
  "serviceCode": "11221 or 131",
  "requestDeliveryReceipt": false
}'