from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from user_app.api.views import register_view, logout_view

urlpatterns = [
    path('login/', ObtainAuthToken.as_view(), name='login'),
    # path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]