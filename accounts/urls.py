from django.urls import path
from .views import LoginUserView, RegisterUserView, ListUserView


urlpatterns=[
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('users/', ListUserView.as_view(), name='listuser'),
]