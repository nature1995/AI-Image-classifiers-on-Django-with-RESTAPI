from django.shortcuts import render,  render_to_response
from gallery.models import Gallery


def home(request):
    gallerys = Gallery.objects
    return render(request, 'home.html', {'gallerys': gallerys})


def page_not_found(request):
    return render_to_response('404.html')


def page_error(request):
    return render_to_response('500.html')








