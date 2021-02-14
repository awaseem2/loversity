from django import forms
from django.db import models

from hello.choices import *

class InputForm(forms.Form):
    name = forms.CharField(max_length=140)
    email = forms.CharField(max_length=140)
    major = forms.CharField(max_length=140)
    age = forms.IntegerField(max_value=120, min_value=18)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gender_choices)
    attractedTo = forms.MultipleChoiceField(
                                       widget=forms.CheckboxSelectMultiple,
                                       choices=gender_choices)
    distance_from_campus = forms.ChoiceField(widget=forms.RadioSelect, choices=distance_choices)
    political_beliefs = forms.ChoiceField(widget=forms.RadioSelect, choices=politics_choices)
    religion  = forms.ChoiceField(widget=forms.RadioSelect, choices=religion_choices)
    do_you_want_someone_who_shares_your_religion = forms.ChoiceField(widget=forms.RadioSelect, choices=share_relig_choices)
    do_you_drink = forms.BooleanField()
    time_spent_in_social_activities = forms.ChoiceField(widget=forms.RadioSelect, choices=social_choices)
    time_spent_partying_pre_covid = forms.ChoiceField(widget=forms.RadioSelect, choices=party_choices)