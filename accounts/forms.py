from dataclasses import field, fields
from wsgiref.validate import validator
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User,Submissions
from django.core.validators import MinValueValidator, MaxValueValidator

class NewUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_organiser')


class NewUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('username', 'email', 'is_organiser')

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = ['title', 'description', 'devfolio_link', 'codebase_link', 'team_name', 'member_name', 'member_email', 'member_phone']

class JudgementForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = ['param1', 'param2', 'param3']
        
class AssignmentForm(forms.Form):
    judge1 = forms.CharField(label="Judge 1 username", max_length=200, required=True)
    judge2 = forms.CharField(label="Judge 2 username", max_length=200, required=True)