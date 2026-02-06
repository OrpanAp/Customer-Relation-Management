from django import forms
from . import models


class DrawForm(forms.ModelForm):
    class Meta:
        model = models.Lead
        fields = '__all__'

