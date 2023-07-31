# accounts/forms.py
from django import forms
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True  # Make the email field required

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email field is required.")
        return email
