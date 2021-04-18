# EMAIL='musthave@and.com' PASSWORD='bemorethan5' PASSWORD='bemorethan5' sh curl-scripts/auth/sign-up.sh

curl "http://localhost:8000/sign-up/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
    "credentials": {
      "email": "'"${EMAIL}"'",
      "password": "'"${PASSWORD}"'",
      "password_confirmation": "'"${PASSWORD}"'"
    }
  }'

echo
