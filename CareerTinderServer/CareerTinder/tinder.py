from django.http import HttpResponse
from django.template import loader
from models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def review_page(request, idx=0):
    idx = int(idx)
    recruiter = Recruiter.objects.all()[0]
    if idx == Hiree.objects.all().count():
        idx = 0
    if request.method == 'POST':
        print("You posted to me.", idx)
        old_idx = idx - 1
        if old_idx < 0: old_idx += Hiree.objects.all().count()
        
        recruiters_encs = Relations.objects.filter(recruiter=recruiter).order_by('encounter_date')
        print("Encounters:")
        for enc in recruiters_encs.all():
            print enc.hiree.name
        enc = recruiters_encs.all()[idx]
        if request.POST['submit_button'] == 'Yes':
            enc.status = '2'
        #elif request.POST['submit_button'] == 'Later':
        #enc.status = 0
        elif request.POST['submit_button'] == 'No':
            enc.status = '1'
        print("New status:", enc.status)
        enc.save()
        return HttpResponseRedirect(reverse("review_page", args=(idx + 1,)))
    else:
        recruiters_encs = Relations.objects.filter(recruiter=recruiter).order_by('encounter_date')
        print("Encounters for fresh page:")
        for enc in recruiters_encs.all():
            print enc.hiree.name
        if recruiters_encs.all().count() == 0:
            template = loader.get_template('CareerTinder/no_page.html')
            context = {
                'name': recruiter.name,
                'message': "You haven't met any candidates yet. Go out and find some recruits!"
            }
            return HttpResponse(template.render(context, request))
        if idx == recruiters_encs.all().count():
            idx = 0

        template = loader.get_template('CareerTinder/review.html')
        hiree = recruiters_encs.all()[idx].hiree
        context = {
            'name': recruiter.name,
            'pic': hiree.face_picture.url,
            'hiree': hiree,
            'hiree_idx': idx
        }
        return HttpResponse(template.render(context, request))

def hiree_thumbnail_page(request, hiree_id=-1):
    recruiter = Recruiter.objects.all()[0]
    if request.method == 'POST':
        print("You posted to me.", idx)
        if request.POST['submit_button'] == 'No':
            encs = Relations.objects.filter(recruiter=recruiter, hiree=int(hiree_id)).delete()
            pass
        return HttpResponseRedirect(reverse("photo"))
    elif hiree_id >= 0:
        encounter = Relations()
        encounter.hiree = Hiree.objects.get(id=int(hiree_id))
        encounter.recruiter = recruiter
        encounter.save()
        template = loader.get_template('CareerTinder/thumbnails.html')
        hiree = encounter.hiree
        context = {
            'name': recruiter.name,
            'pic': hiree.face_picture.url,
            'hiree': hiree,
        }
        return HttpResponse(template.render(context, request))
    template = loader.get_template('CareerTinder/no_page.html')
    context = {
        'name': recruiter.name,
        'message': "Invalid parameters to the thumbnails page."
    }
    return HttpResponse(template.render(context, request))


def browse(request):
    template = loader.get_template('CareerTinder/browse.html')
    
    recruiter = Recruiter.objects.all()[0]

    hirees_list = []
    pics = []
    id_idx = {}
    recruiters_encs = Relations.objects.filter(recruiter=recruiter).order_by('encounter_date')
    for i, encounter in enumerate(recruiters_encs):
        try:
            if encounter.hiree not in hirees_list:
                hirees_list.append(encounter.hiree)
                pics.append(encounter.hiree.face_picture)
                id_idx[encounter.hiree.id] = i
        except Hiree.DoesNotExist:
            print("Hiree {} does not exist in the database.".format(hiree))
    context = {
        'name': recruiter.name,
        'pics': pics,
        'hirees': hirees_list,
        'id_idx': id_idx
    }
    return HttpResponse(template.render(context, request))

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)