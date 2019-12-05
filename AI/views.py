from django.shortcuts import render
from gallery.models import Gallery


def home(request):
    gallerys = Gallery.objects
    return render(request, 'home.html', {'gallerys': gallerys})


def handler404(request, exception):
    return render('home.html')


def handler500(request):
    return render('home.html')








