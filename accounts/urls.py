from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import CustomSignupView

urlpatterns = [
    # Other URL patterns...
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accounts/login/', LoginView.as_view(template_name='account/login.html'), name='account_login'),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
]
