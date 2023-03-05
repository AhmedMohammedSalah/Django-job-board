from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """Form definition for SignUpForm."""

    class Meta:
        """Meta definition for SignUpForm."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']
