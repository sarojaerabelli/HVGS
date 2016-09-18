# -*- coding: utf-8 -*-
from django import forms


class ResumeForm(forms.Form):
    resume_picture = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
