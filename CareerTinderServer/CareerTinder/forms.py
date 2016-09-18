# -*- coding: utf-8 -*-
from django import forms
from material import *
from CareerTinder.models import DEGREE_CHOICES


class InputHireeForm(forms.Form):
    name = forms.CharField(max_length=50, label='Name:', help_text='First and last please')
    email = forms.CharField(max_length=50, label='Email:', help_text='i.e. example@hyre.com')
    college = forms.CharField(max_length=50, label='College:', help_text='Make sure you spell it allll out')
    degree = forms.CharField(max_length=10, label='Degree Type:', widget=forms.Select(choices=DEGREE_CHOICES))
    year = forms.CharField(max_length=50, label='Graduation Year:')
    major = forms.CharField(max_length=50, label='Major:')

    resume_picture = forms.FileField(label='Upload your resume as a pdf...')
    face_picture = forms.FileField(label='Upload a clear picture of your face...')

    layout = Layout('name', 'email', 'college',
        Row('major', 'year', 'degree'),
        'resume_picture', 'face_picture')
