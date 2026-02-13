from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, UsernameField


class DrawForm(forms.ModelForm):
    class Meta:
        model = models.Lead
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'password1', 'password2',)
        field_classes = {'username': UsernameField}
        
        
class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=models.Agent.objects.none())
    
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        agents = models.Agent.objects.filter(organization=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents
        
        
    
class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Lead
        fields = ('category',)