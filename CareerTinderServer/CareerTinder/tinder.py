from django.http import HttpResponse
from django.template import loader
from models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def review_page(request, idx=0):
    idx = int(idx)
    if idx == Hiree.objects.all().count():
        idx = 0
    if request.method == 'POST':
        print("You posted to me.", idx)
        recruiter = Recruiter.objects.get(id=1)
        if request.POST['submit_button'] == 'Yes':
            return HttpResponseRedirect(reverse("review_page", args=(idx + 1,)))
        elif request.POST['submit_button'] == 'No':
            return HttpResponseRedirect(reverse("review_page", args=(idx + 1,)))
    else:
        template = loader.get_template('CareerTinder/review.html')
        
        recruiter = Recruiter.objects.get(id=1)

        try:
            hiree = Hiree.objects.get(id=recruiter.hirees[idx])
        except Hiree.DoesNotExist:
            print("Hiree {} does not exist in the database.".format(hiree))
        context = {
            'name': recruiter.name,
            'pic': hiree.face_picture.url,
            'hiree_idx': idx
        }
        return HttpResponse(template.render(context, request))

def browse(request):
    template = loader.get_template('CareerTinder/browse.html')
    
    recruiter = Recruiter.objects.get(id=1)

    hirees_list = []
    pics = []
    for hiree in recruiter.hirees:
        try:
            obj = Hiree.objects.get(id=hiree)
            hirees_list.append(hiree)
            pics.append(obj.face_picture)
        except Hiree.DoesNotExist:
            print("Hiree {} does not exist in the database.".format(hiree))
    context = {
        'name': recruiter.name,
        'pics': pics,
        'hirees': hirees_list
    }
    return HttpResponse(template.render(context, request))
