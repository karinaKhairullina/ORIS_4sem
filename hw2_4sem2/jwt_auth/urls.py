from django.urls import path
from .views import UserLoginAPIView, UserRegistrationAPIView, UserAuthAPIView

urlpatterns = [
    path('api/login/', UserLoginAPIView.as_view(), name='login'),
    path('api/register/', UserRegistrationAPIView.as_view(), name='register'),
    path('api/auth/', UserAuthAPIView.as_view(), name='auth'),
]









