#!/usr/bin/bash

# Get token from MTN API

curl -X POST -H "Content-Type: application/x-www-form-urlencoded" https://api.mtn.com/v1/oauth/access_token?grant_type=client_credentials -d 'client_id=2TtOY4OBR0qaGefDLA4GGDvgt1ZxvN3Y&client_secret=9nA2IUEQjiYHoGqp'