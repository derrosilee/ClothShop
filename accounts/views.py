from allauth.account.views import SignupView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class CustomSignupView(SignupView):
    def form_valid(self, form):
        email = form.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            # Email already exists in the database
            messages.error(self.request, "An account with this email already exists.")
            return redirect(reverse_lazy('account_signup'))
        return super().form_valid(form)
