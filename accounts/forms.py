from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    """Form definition for SignUpForm."""

    class Meta:
        """Meta definition for SignUpForm."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class UserForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = User
        fields = ['username','first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Profile
        fields = ['phone','city','image']

