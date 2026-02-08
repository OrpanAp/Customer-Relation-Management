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
        fields = ('username',)
        field_classes = {'username': UsernameField}