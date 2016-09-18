# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from CareerTinder.models import Hiree
from CareerTinder.forms import InputHireeForm
from django.shortcuts import render
import os


def upload_resume(request):
    # Handle file upload
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        form = InputHireeForm(request.POST, request.FILES)
        if form.is_valid():
            newhiree = Hiree(name=request.POST.get('name'),
                             email=request.POST.get('email'),
                             college=request.POST.get('college'),
                             # degree=request.POST.get('degree'),
                             year=request.POST.get('year'),
                             major=request.POST.get('major'),
                             resume_picture=request.FILES['resume_picture'],
                             face_picture=request.FILES['face_picture'])
            newhiree.save()

            # call javascript function
                        


            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('upload_resume'))
    else:
        form = InputHireeForm()  # A empty, unbound form

    # Load hirees for the list page
    hirees = Hiree.objects.all()

    # Render list page with the documents and the form
    return render(request,
        'CareerTinder/upload.html',
        {'hirees': hirees, 'form': form}
    )
