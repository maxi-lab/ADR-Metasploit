from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import PingView, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]
