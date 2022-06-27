from django.urls import path, include
from accounts.api.views import registration_view, account_view

urlpatterns = [
    path('register/',  registration_view),
    path( 'detail/', account_view )
]
