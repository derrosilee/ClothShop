from django.shortcuts import render
from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from allauth.account.views import PasswordChangeView, PasswordSetView
from allauth.account.views import PasswordResetView, PasswordResetDoneView, PasswordResetFromKeyView, \
    PasswordResetFromKeyDoneView
from allauth.account.views import LoginView, LogoutView


class CustomSignupView(SignupView):
    template_name = 'account/signup.html'


class CustomLoginView(LoginView):
    template_name = 'account/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'account/logout.html'


@login_required
def profile(request):
    return render(request, 'account/profile.html')


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'account/password_change.html'


class CustomPasswordSetView(PasswordSetView):
    template_name = 'account/password_set.html'


class CustomPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    template_name = 'account/password_reset_from_key.html'


class CustomPasswordResetFromKeyDoneView(PasswordResetFromKeyDoneView):
    template_name = 'account/password_reset_from_key_done.html'
