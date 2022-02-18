from django.conf import settings
from django.urls import path

from dj_rest_auth.views import (EmailCreateView, EmailDestroyView, EmailListView, EmailSetPrimaryView, EmailVerifyView, LoginView,
                                LogoutView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView, UserDetailsView, CheckVerificationEmailView)

urlpatterns = [
    # URLs that do not require a session or valid token
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('login/', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('email/', EmailListView.as_view(), name='rest_email_list'),
    path('email/<int:pk>/', EmailDestroyView.as_view(), name='rest_email_destroy'),
    path('email/<int:pk>/verify/', EmailVerifyView.as_view(), name='rest_email_verify'),
    path('email/<str:key>/check-verification/', CheckVerificationEmailView.as_view(), name="rest_email_check_verification"),
    path('email/<int:pk>/primary/', EmailSetPrimaryView.as_view(), name='rest_email_primary'),
    path('email/create/', EmailCreateView.as_view(), name='rest_email_create'),
]

if getattr(settings, 'REST_USE_JWT', False):
    from rest_framework_simplejwt.views import TokenVerifyView

    from dj_rest_auth.jwt_auth import get_refresh_view

    urlpatterns += [
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    ]
