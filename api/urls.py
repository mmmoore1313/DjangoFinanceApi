from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.account_views import Accounts, AccountDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('accounts/', Accounts.as_view(), name='accounts'),
    path('accounts/<int:pk>/', AccountDetail.as_view(), name='account_detail'),
]
