from django import forms
from .models import MiniURL


class URlForm(forms.Form):
    url_form = forms.URLField(label='Enter the URL', max_length=150)
    identifier_form = forms.CharField(label='Identified', max_length=100)



