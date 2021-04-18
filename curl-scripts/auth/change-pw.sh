# TOKEN=<token> OLDPW=<oldPW> NEWPW=<newPW> sh curl-scripts/auth/change-pw.sh

curl "http://localhost:8000/change-password/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "passwords": {
      "old": "'"${OLDPW}"'",
      "new": "'"${NEWPW}"'"
    }
  }'

echo
