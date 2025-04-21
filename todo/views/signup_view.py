from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignupView(CreateView):
    """
    View to handle user registration.
    Uses Django's built-in UserCreationForm to create a new user account.

    Attributes:
        form_class (UserCreationForm): The form used for user signup.
        template_name (str): The template that renders the signup form.
        success_url (str): The URL to redirect to after successful registration.
    """
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
