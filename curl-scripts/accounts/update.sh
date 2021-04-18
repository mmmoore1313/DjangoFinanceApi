#!/bin/bash
# TOKEN='<token>' ID='<accountID>' NAME='<accntName>' TYPE='accntType' VALUE='<NumberWithTwoDecimals' sh curl-scripts/accounts/update.sh

curl "http://localhost:8000/accounts/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "account": {
      "name": "'"${NAME}"'",
      "type": "'"${TYPE}"'",
      "amount": "'"${AMOUNT}"'"
    }
  }'

echo
