from django import forms
from leads.models import Agent



class AgentCreationForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ('user', )