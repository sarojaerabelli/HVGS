from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,
        'CareerTinder/index.html'
    )


def about(request):
    return render(request,
        'CareerTinder/about.html'
    )


def error404(request):
    template = loader.get_template('CareerTinder/no_page.html')
    context = {
        'message': "Oops, looks like this HackMIT team needed the 404 page after all."
    }
    return HttpResponse(template.render(context, request))
