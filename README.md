
# Where's My Money?
> | Contents |  |
> |--|--|
> | [About](https://github.com/mmmoore1313/DjangoFinanceApi#about-app) | [Technologies Used](https://github.com/mmmoore1313/DjangoFinanceApi#technologies-employed) |
> | [Routes](https://github.com/mmmoore1313/DjangoFinanceApi#catalogue-of-routes) | [Future Iterations](https://github.com/mmmoore1313/DjangoFinanceApi#future-iterations) |
> |[ERD](https://github.com/mmmoore1313/DjangoFinanceApi#entity-relationship-diagram-or-wireframe) | [Links](https://github.com/mmmoore1313/DjangoFinanceApi#links) |
> | [Planning](https://github.com/mmmoore1313/DjangoFinanceApi#planning) |  |
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
>>> | GET |  | index or list | (R)ead |
>>> | GET |  | show or retrieve | (R)ead |
>>> | PATCH |  | update | (U)pdate |
>>> | DELETE |  | destroy | (D)elete |
>>>
>>> #### Curl-Scripts
>>> | Action | JSON | Command | Success | Failure | 
>>> |--|--|--|--|--|
>>> | sign-up | ``'{ '"credentials": { "email": "'"${EMAIL}"'", "password": "'"${PASSWORD}"'", "password_confirmation": "'"${PASSWORD}"'" } }'`` | ``EMAIL='musthave@and.com' PASSWORD='bemorethan5' PASSWORD='bemorethan5' sh curl-scripts/auth/sign-up.sh``| `201 Created` | `401 Not Found` |
>>> | sign-in | ``'{ "credentials": { "email": "'"${EMAIL}"'", "password": "'"${PASSWORD}"'" } }'`` | ``EMAIL='musthave@and.com' PASSWORD='bemorethan5' sh curl-scripts/auth/sign-in.sh`` | `201 Created` | `401 Not Found` |
>>> |  |  |  | `201 Created` | `401 Not Found` |
>>> |  |  |  | `201 Created` | `401 Not Found` |
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
>>> | PATCH |  | update | (U)pdate |
>>> | DELETE | /accounts/:id | destroy | (D)elete |
>>>
>>> #### Curl-Scripts
>>> | Action | JSON | Command | Success | Failure | 
>>> |--|--|--|--|--|
>>> | create account | ``'{ "account": { "name": "'"${NAME}"'", "type": "'"${TYPE}"'", "value": "'"${VALUE}"'" } }'`` | ``TOKEN='<token>' NAME='<accntName>' TYPE='accntType' VALUE='<NumberWithTwoDecimals' sh curl-scripts/accounts/create.sh`` | `201 Created` | `401 Not Found` |
>>> | index accounts |  | ``TOKEN='<token>' sh curl-scripts/accounts/index.sh`` | `200 OK` | `401 Not Found` |
>>> | show account |  | ``TOKEN='<token>' ID='<accountID>' sh curl-scripts/accounts/show.sh`` | `200 OK` | `404 Not Found` |
>>> | update account | ``'{ "account": { "name": "'"${NAME}"'", "type": "'"${TYPE}"'", "value": "'"${VALUE}"'" } }'`` | ``TOKEN='<token>' ID='<accountID>' NAME='<accntName>' TYPE='accntType' VALUE='<NumberWithTwoDecimals' sh curl-scripts/accounts/update.sh`` | `200 OK` | `400 Bad Request` |
>>> | delete account |  | ``TOKEN='<token>' ID='<accountID>' sh curl-scripts/accounts/delete.sh`` | `201 Created` | `401 Not Found` |
>
> ###### [(Return to top)](https://github.com/mmmoore1313/DjangoFinanceApi#wheres-my-money)
>
> ## Entity Relationship Diagram
> ![ERD](https://media.git.generalassemb.ly/user/33705/files/cb2ee980-9c53-11eb-9539-137e2c2bd992)
>
> ### snapshot of app
>
> ###### [(Return to top)](https://github.com/mmmoore1313/DjangoFinanceApi#wheres-my-money)
>
> ## Planning
>> <!-- Desctiption -->
>>
>>> |  | **Day 1:** | **Day 2:** | **...**
>>> |--|--|--|--|
>>> | Description | <!-- Description --> | <!-- Description --> | <!-- Description --> |
>>> | [Teamate]() | <!-- What they did --> | <!-- What they did -->  | <!-- What they did -->  |
>>> | [Teamate]() | <!-- What they did --> | <!-- What they did -->  | <!-- What they did -->  |
>
>
> ###### [(Return to top)](https://github.com/mmmoore1313/DjangoFinanceApi#wheres-my-money)
>
> ## Technologies Employed
>> | **General Development** | **[Client]() Development** | **[API]() Development** | **Deployment** |
>> |--|--|--|--|
>> | [Technology Name](docs) | [Technology Name](docs) | [Technology Name](docs) | [Technology Name](docs) |
>
>
> ###### [(Return to top)](https://github.com/mmmoore1313/DjangoFinanceApi#wheres-my-money)
>
> ## Future Iterations
> <!-- Desctiption -->
>
>
> ###### [(Return to top)](https://github.com/mmmoore1313/DjangoFinanceApi#wheres-my-money)
>
> ## Links
>> | | **Deployed Sites** | **Repositories** |
>> |--|--|--|
>> | Front End App: | [appUrl](appUrl) | [DjangoFinanceApi](https://github.com/mmmoore1313/DjangoFinanceApi) |
>> | Database App | [dbUrl](dbUrl) | [DjangoFinanceApi](https://github.com/mmmoore1313/DjangoFinanceApi) |
>
> ###### [(Return to top)](https://github.com/mmmoore1313/DjangoFinanceApi#wheres-my-money)
>
