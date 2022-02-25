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
        fields = ['title', 'description', 'devfolio_link', 'codebase_link', 'primary_track', 'secondary_track', 'team_name', 'member_name', 'member_email', 'member_phone']

class JudgementForm(forms.Form):
    validator1 = [ MinValueValidator(0), MaxValueValidator(10)]
    validator2 = [ MinValueValidator(0), MaxValueValidator(20)]
    param_1 = forms.IntegerField(validators=validator1,required=True, label="ORIGINALITY OF IDEA/ ADVANCEMENTS IN THE FIELD (10 MARKS)", help_text="Consider the novelty of the solution or how different/better from existing solutions. Or the “wow” factor of the idea.", widget=forms.TextInput(attrs={'class': "form-control m-20", 'style': "margin-top:10px;"})) 
    param_2 = forms.IntegerField(validators=validator1,required=True, label="BUSINESS VALUE / SOCIETAL IMPACT (10 MARKS)", help_text="If a solution is a social service-related app, the societal impact of the hack is evaluated.  Whereas, in the case of a commercial product-related hack, the hack is evaluated on whether a profitable & realistic commercial product can be made out of the solution or if it positively impacts society.") 
    param_3 = forms.IntegerField(validators=validator2,required=True, label="IMPLEMENTATION OF IDEA (20 MARKS)", help_text="Consider the Approach to the problem, Technological Complexity, System Design and User Experience") 
    param_4 = forms.IntegerField(validators=validator1,required=True, label="QUALITY OF PRESENTATION (10 MARKS)", help_text="Explanation of the hack done and the creativity involved in presenting the hack. The evaluation must consider the video and other media content in the submission.") 
    param_5 = forms.IntegerField(validators=validator1, required=False ,label="RELEVANCE TO PRIMARY TRACK (10 MARKS)", help_text="Evaluate based on how relevant the project is with respect to the track chosen. This is considered to decide track prizes.") 
    param_6 = forms.IntegerField(validators=validator1, required=False ,label="RELEVANCE TO SECONDARY TRACK (10 MARKS)", help_text="Evaluate based on how relevant the project is with respect to the track chosen. This is considered to decide track prizes.") 
        
class AssignmentForm(forms.Form):
    judge1 = forms.CharField(label="Judge 1 username", max_length=200, required=True)
    judge2 = forms.CharField(label="Judge 2 username", max_length=200, required=True)