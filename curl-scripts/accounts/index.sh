#!/bin/bash
# TOKEN='<token>' sh curl-scripts/accounts/index.sh

curl "http://localhost:8000/accounts/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
