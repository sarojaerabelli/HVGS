from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('CareerTinder/review.html')
    context = {
        'name': 'John Doe'
    }
    return HttpResponse(template.render(context, request))
