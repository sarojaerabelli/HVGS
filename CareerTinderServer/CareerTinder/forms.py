# -*- coding: utf-8 -*-
from django import forms


class InputHireeForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='First Name:')
    last_name = forms.CharField(max_length=50, label='Last Name:')
    college = forms.CharField(max_length=50, label='College:')
    degree = forms.CharField(max_length=50, label='Degree Type:',
        help_text='highest degree completed')
    year = forms.CharField(max_length=50, label='Graduation Date:',
        help_text='estimated graduation date')
    major = forms.CharField(max_length=50, label='Major:')

    resume_picture = forms.FileField(
        label='Select a resume file',
        help_text='max. 42 megabytes'
    )

    face_picture = forms.FileField(
        label='Select a face file',
        help_text='max. 42 megabytes'
    )
