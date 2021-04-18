#!/bin/bash
# TOKEN='<token>' NAME='<accntName>' TYPE='accntType' VALUE='<NumberWithTwoDecimals' sh curl-scripts/accounts/create.sh

curl "http://localhost:8000/accounts/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "account": {
      "name": "'"${NAME}"'",
      "type": "'"${TYPE}"'",
      "value": "'"${VALUE}"'"
    }
  }'

echo
