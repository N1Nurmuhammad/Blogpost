from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', registration_view, name= 'signup'),
    path('login/', account_authentication, name='login'),
    path('logout/', logout_view, name='logout'),
    path('update/<int:pk>', edit_account_view, name='update'),
]

