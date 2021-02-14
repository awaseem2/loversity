from django import forms
from django.db import models

class InputForm(forms.Form):
    input_name = forms.CharField(max_length=140)
    input_major = forms.CharField(max_length=140)