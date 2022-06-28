from django.urls import path, include
from accounts.api.views import registration_view, account_view, update_account_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/',  registration_view),
    path( 'detail/', account_view ),
    path('update/', update_account_view),
    path('login/', obtain_auth_token),


]
