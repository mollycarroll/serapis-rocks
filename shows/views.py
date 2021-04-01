from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Show, Musician, Photo, HomeText, LatestVideo, Video


def index(request):
    show_list = Show.objects.order_by('show_date')[:1]
    members = Musician.objects.order_by('name')
    home_text = HomeText.objects.all()
    latest_video = LatestVideo.objects.all()
    context = {
        'show_list': show_list,
        'members': members,
        'home_text': home_text,
        'latest_video': latest_video,
    }
    return render(request, 'shows/index.html', context)

def showdates(request):
    show_list = Show.objects.order_by('show_date')

    context = {
        'show_list': show_list,
    }

    return render(request, 'shows/showdates.html', context)


def music(request):
    video_list = Video.objects.all()

    context = {
        'video_list': video_list,
    }

    return render(request, 'shows/music.html', context)
    

def photos(request):
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'shows/photos.html', context)