from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Show, Musician, Photo


def index(request):
    show_list = Show.objects.order_by('show_date')[:1]
    members = Musician.objects.order_by('name')
    context = {
        'show_list': show_list,
        'members': members,
    }
    return render(request, 'shows/index.html', context)


def photos(request):
    photos = Photo.objects.order_by('date')

    context = {
        'photos': photos,
    }

    return render(request, 'shows/photos.html', context)