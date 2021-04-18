#!/bin/bash
# TOKEN='<token>' ID='<accountID>' sh curl-scripts/accounts/show.sh

curl "http://localhost:8000/accounts/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
