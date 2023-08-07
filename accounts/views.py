from django.contrib.auth.models import User
from allauth.account.views import SignupView
from allauth.exceptions import ImmediateHttpResponse
from allauth.account import signals
from allauth.utils import get_username_max_length

class CustomSignupView(SignupView):
    def form_valid(self, form):
        email = form.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            # Email already exists in the database
            raise ImmediateHttpResponse(self.response_email_exists())
        return super().form_valid(form)

    def response_email_exists(self):
        # Customize the error message to display to the user
        error_message = "An account with this email already exists."
        signals.email_confirmation_sent.send(sender=self.form.email_confirmation_email)
        self.add_message(self.request, messages.ERROR, error_message)
        return self.render_to_response(self.get_context_data())
