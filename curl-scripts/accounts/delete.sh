#!/bin/bash
# TOKEN='<token>' ID='<accountID>' sh curl-scripts/accounts/delete.sh

curl "http://localhost:8000/accounts/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
