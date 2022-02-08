from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class NewUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_organiser')


class NewUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('username', 'email', 'is_organiser')