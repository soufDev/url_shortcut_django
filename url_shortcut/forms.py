from django import forms
from .models import MiniURL


class URlForm(forms.Form):

    class Meta:
        model = MiniURL
        fields = ('default_url', 'identifier_create')



