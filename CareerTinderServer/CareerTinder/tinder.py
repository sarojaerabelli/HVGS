from django.http import HttpResponse
from django.template import loader
from models import *

# Create your views here.
def index(request):
    template = loader.get_template('CareerTinder/review.html')
    
    recruiter = Recruiter.objects.get(id=1)
    
    context = {
        'name': recruiter.name,
        'photo_urls': [hiree.face_picture for hiree in recruiter.interested_hirees]
    }
    return HttpResponse(template.render(context, request))
