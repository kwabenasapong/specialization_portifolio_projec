#!/usr/bin/env bash

# API for Hubtel's quick sms api

curl -i -X GET \
  'https://smsc.hubtel.com/v1/messages/send?clientsecret=fhanifdw&clientid=hiljcvrg&from=Test_sms&to=0202419977&content=This+Is+A+Test+Message' 
