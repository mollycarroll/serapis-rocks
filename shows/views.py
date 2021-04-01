from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Show, Musician, Photo, HomeText


def index(request):
    show_list = Show.objects.order_by('show_date')[:1]
    members = Musician.objects.order_by('name')
    home_text = HomeText.objects.all()
    context = {
        'show_list': show_list,
        'members': members,
        'home_text': home_text,
    }
    return render(request, 'shows/index.html', context)


def photos(request):
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'shows/photos.html', context)