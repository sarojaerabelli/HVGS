# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from CareerTinder.models import Hiree
from CareerTinder.forms import ResumeForm
from django.shortcuts import render


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Hiree(resume_picture=request.FILES['resume_picture'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = ResumeForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Hiree.objects.all()

    # Render list page with the documents and the form
    return render(request,
        'CareerTinder/upload.html',
        {'documents': documents, 'form': form}
    )
