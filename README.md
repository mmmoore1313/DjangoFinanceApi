
# Where's My Money?
> | Contents |  |
> |--|--|
> | [About](https://github.com/mmmoore1313/DjangoFinanceApi#about-app) | [Technologies Used](https://github.com/mmmoore1313/DjangoFinanceApi#technologies-employed) |
> | [Routes](https://github.com/mmmoore1313/DjangoFinanceApi#catalogue-of-routes) | [Future Iterations](https://github.com/mmmoore1313/DjangoFinanceApi#future-iterations) |
> |[ERD](https://github.com/mmmoore1313/DjangoFinanceApi#entity-relationship-diagram-or-wireframe) | [Links](https://github.com/mmmoore1313/DjangoFinanceApi#links) |
>
>
> ## About App
> This is the Django based API for the Where's My Money app. This Django app was made using the template provided to the students of the General Assembly Software Engineering Immersive.
>
> ## Catalogue of Routes
>> ### Auth Routes 
>>> | HTTP Method | URL Path | Action | CRUD |
>>> |--|--|--|--|
>>> | POST | /sign-up/ | create | (C)reate |
>>> | GET | /sign-in/ | show or retrieve | (R)ead |
>>> | PATCH | /change-password/ | update | (U)pdate |
>>> | DELETE | /sign-out/ | destroy | (D)elete |
>>>
>>> #### Curl-Scripts
>>> | Action | JSON | Command | Success | Failure | 
>>> |--|--|--|--|--|
>>> | sign-up | ``'{ '"credentials": { "email": "'"${EMAIL}"'", "password": "'"${PASSWORD}"'", "password_confirmation": "'"${PASSWORD}"'" } }'`` | ``EMAIL='musthave@and.com' PASSWORD='bemorethan5' PASSWORD='bemorethan5' sh curl-scripts/auth/sign-up.sh``| `201 Created` | `401 Not Found` |
>>> | sign-in | ``'{ "credentials": { "email": "'"${EMAIL}"'", "password": "'"${PASSWORD}"'" } }'`` | ``EMAIL='musthave@and.com' PASSWORD='bemorethan5' sh curl-scripts/auth/sign-in.sh`` | `201 Created` | `401 Not Found` |
>>> | change-password | ``'{ "passwords": { "old": "'"${OLDPW}"'", "new": "'"${NEWPW}"'" } }'`` | ``TOKEN=<token> OLDPW=<oldPW> NEWPW=<newPW> sh curl-scripts/auth/change-pw.sh`` | `201 Created` | `401 Not Found` |
>>> | sign-out |  | ``TOKEN=<token> sh curl-scripts/auth/sign-out.sh`` | `201 Created` | `401 Not Found` |
>>
>>
>> ###### [(Return to top)](https://github.com/mmmoore1313/DjangoFinanceApi#wheres-my-money)
>>
>> ### Other Routes 
>>> | HTTP Method | URL Path | Action | CRUD |
>>> |--|--|--|--|
>>> | POST | /accounts/ | create | (C)reate |
>>> | GET | /accounts/ | index or list | (R)ead |
>>> | GET | /accounts/:id | show or retrieve | (R)ead |
>>> | PATCH | /accounts/:id | update | (U)pdate |
>>> | DELETE | /accounts/:id | destroy | (D)elete |
>>>
>>> #### Curl-Scripts
>>> | Action | JSON | Command | Success | Failure | 
>>> |--|--|--|--|--|
>>> | create account | ``'{ "account": { "name": "'"${NAME}"'", "type": "'"${TYPE}"'", "amount": "'"${AMOUNT}"'" } }'`` | ``TOKEN='<token>' NAME='<accntName>' TYPE='accntType' AMOUNT='<NumberWithTwoDecimals' sh curl-scripts/accounts/create.sh`` | `201 Created` | `401 Not Found` |
>>> | index accounts |  | ``TOKEN='<token>' sh curl-scripts/accounts/index.sh`` | `200 OK` | `401 Not Found` |
>>> | show account |  | ``TOKEN='<token>' ID='<accountID>' sh curl-scripts/accounts/show.sh`` | `200 OK` | `404 Not Found` |
>>> | update account | ``'{ "account": { "name": "'"${NAME}"'", "type": "'"${TYPE}"'", "amount": "'"${AMOUNT}"'" } }'`` | ``TOKEN='<token>' ID='<accountID>' NAME='<accntName>' TYPE='accntType' AMOUNT='<NumberWithTwoDecimals' sh curl-scripts/accounts/update.sh`` | `200 OK` | `400 Bad Request` |
>>> | delete account |  | ``TOKEN='<token>' ID='<accountID>' sh curl-scripts/accounts/delete.sh`` | `201 Created` | `401 Not Found` |
>
> ###### [(Return to top)](https://github.com/mmmoore1313/DjangoFinanceApi#wheres-my-money)
>
> ## Entity Relationship Diagram
> ![ERD](https://media.git.generalassemb.ly/user/33705/files/cb2ee980-9c53-11eb-9539-137e2c2bd992)
>
>
> ###### [(Return to top)](https://github.com/mmmoore1313/DjangoFinanceApi#wheres-my-money)
>
> ## Technologies Employed
>> | **General Development** | **[Client](https://github.com/mmmoore1313/WheresMyMoney-client) Development** | **[API](https://github.com/mmmoore1313/DjangoFinanceApi) Development** | **Deployment** |
>> |--|--|--|--|
>> | [GitHub](https://github.com/) | [React](https://reactjs.org/) | [Express](https://expressjs.com) | [GH Pages](https://pages.github.com/) |
>> | [Atom](https://atom.io/) | [React-Bootstrap](https://react-bootstrap.github.io/) | [Postman](https://www.postman.com/) | [Heroku](https://www.heroku.com) |
>> | [VS Code](https://code.visualstudio.com/) | [Semantic UI React](https://react.semantic-ui.com/) | [Django](https://docs.djangoproject.com/en/3.2/) | |
>> | [GoogleSheets](https://docs.google.com/spreadsheets/d/1kJRGhsgKEV9xVL3lXtyz6cqBWf14lm6JuXD02uneldA/edit#gid=0) | | | |
>> | [Google](https://www.google.com/) | | | |
>> | [MDN Web Docs](https://developer.mozilla.org/en-US/) | | | |
>> | [JavaScript](https://www.javascript.com/) | | | |
>> | [CSS](https://www.w3schools.com/css/) | | | |
>> | [SCSS](https://sass-lang.com/) | | | |
>
> ###### [(Return to top)](https://github.com/mmmoore1313/DjangoFinanceApi#wheres-my-money)
>
> ## Future Iterations
>> V1: 
>>> - A User has the ability to make accounts of varrying types that can display the amount the user has entered.
>> 
>> V2:
>>> - A User can update the amount in the account by adding Income or subtracting expenses
>>>> - Income and expenses will have date/time stamps
>>>> - Income and expenses will have the standard CRUD actions
>>>> - Income and expenses will be viewable (in a list)
>>
>> V3:
>>> - A User can search the Accounts for previous entries
>>>> - Income, expenses will be searchable by amount, type, name, and date
>>
>> ###### [(Return to top)](https://github.com/mmmoore1313/DjangoFinanceApi#wheres-my-money)
>
> ## Links
>> | | **Deployed Sites** | **Repositories** |
>> |--|--|--|
>> | Front End App: | [WheresMyMoney](https://mmmoore1313.github.io/WheresMyMoney-client/) | [WheresMyMoney-client](https://github.com/mmmoore1313/WheresMyMoney-client) |
>> | Database App | [dbUrl](dbUrl) | [DjangoFinanceApi](https://github.com/mmmoore1313/DjangoFinanceApi) |
>
> ###### [(Return to top)](https://github.com/mmmoore1313/DjangoFinanceApi#wheres-my-money)
>
