
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import PingView


urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
]
