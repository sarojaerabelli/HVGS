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
            print enc.hiree.first_name + " " + enc.hiree.last_name
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
            print enc.hiree.first_name + " " + enc.hiree.last_name
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
