from django import forms
from django.contrib.auth.models import User
from allauth.account.views import SignupView
from allauth.exceptions import ImmediateHttpResponse
from allauth.account import signals
from allauth.account.forms import SignupForm
from django.contrib import messages

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

class CustomSignupView(SignupView):
    form_class = CustomSignupForm  # Use the custom form class

    def form_valid(self, form):
        # Handle successful form submission
        response = super().form_valid(form)
        # You can add custom actions here if needed
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom context data if needed
        return context
