from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserListView,
    UserCreateApi,
    LoginAPIView,
    SendEmailVerificationCodeAPIView,
    VerifyEmailCode,
)

router = DefaultRouter()
router.register(r'', UserListView, basename='users')

urlpatterns = [
    path('register/', UserCreateApi.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('test-email/', SendEmailVerificationCodeAPIView.as_view(), name='send-email'),
    path('verify-email/', VerifyEmailCode.as_view(), name='verify-email'),
]

urlpatterns += router.urls

