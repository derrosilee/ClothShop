# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.CustomLoginView.as_view(), name='account_login'),
    path('logout/', views.CustomLogoutView.as_view(), name='account_logout'),
    path('password/change/', views.CustomPasswordChangeView.as_view(), name='account_change_password'),
    path('password/set/', views.CustomPasswordSetView.as_view(), name='account_set_password'),
    path('password/reset/', views.CustomPasswordResetView.as_view(), name='account_reset_password'),
    path('password/reset/done/', views.CustomPasswordResetDoneView.as_view(), name='account_reset_password_done'),
    path('password/reset/key/<uidb36>/<key>/', views.CustomPasswordResetFromKeyView.as_view(), name='account_reset_password_from_key'),
    path('password/reset/key/done/', views.CustomPasswordResetFromKeyDoneView.as_view(), name='account_reset_password_from_key_done'),
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),
    # Add other URL patterns for registration, password reset, etc., as needed
]
