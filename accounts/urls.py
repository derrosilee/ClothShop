from django.urls import path
from allauth.account.views import PasswordResetView, LogoutView, LoginView

from accounts import views
from accounts.views import CustomSignupView

urlpatterns = [
    # Other URL patterns...
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('password/reset/', PasswordResetView.as_view(template_name='account/password_reset.html'),
         name='account_reset_password'),

    path('dashboard/', views.dashboard, name='dashboard'),

]
