from django.http import HttpResponse
from django.template import loader
import os
import json

# Create your views here.
def index(request):
    template = loader.get_template('CareerTinder/retrieve.html')
    context = {
        'name': 'John Doe'
    }
    return HttpResponse(template.render(context, request))

def face_list(request):
    return HttpResponse(json.dumps([file for file in os.listdir("media/media/faces") if ".jpg" in file.lower() or ".png" in file.lower()]))