from django.http import HttpResponse
from django.template import loader
from models import *

# Create your views here.
def index(request):
    template = loader.get_template('CareerTinder/review.html')
    
    recruiter = Recruiter.objects.get(id=1)
    
    face_pictures = []
    for hiree in recruiter.hirees:
        try:
            pic = Hiree.objects.get(id=hiree)
            face_pictures.append(pic.face_picture.url)
        except Hiree.DoesNotExist:
            print("Hiree {} does not exist in the database.".format(hiree))
    print("Pictures:", face_pictures)
    context = {
        'name': recruiter.name,
        'photo_urls': face_pictures
    }
    return HttpResponse(template.render(context, request))
