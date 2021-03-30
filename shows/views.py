from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Show, Musician


def index(request):
    show_list = Show.objects.order_by('show_date')
    members = Musician.objects.order_by('name')
    context = {
        'show_list': show_list,
        'members': members,
    }
    return render(request, 'shows/index.html', context)
