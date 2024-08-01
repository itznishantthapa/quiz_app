from django.contrib import admin
from django.urls import include, path

from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ResendEmailVerificationView
from dj_rest_auth.views import LoginView
from .views import email_confirm_redirect

urlpatterns = [
    path('register/', RegisterView.as_view(), name='rest_register'),
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('resend-email/', ResendEmailVerificationView.as_view(),
         name="rest_resend_email"),
    path('account-confirm-email/<str:key>',
         email_confirm_redirect, name='account_confirm_email'),
    path('account-email-verification-sent/', VerifyEmailView.as_view(),
         name='account_email_verification_sent'),
    path('login/', LoginView.as_view(), name='rest_login')
]
