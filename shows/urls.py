from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'shows'

urlpatterns = [
    path('', views.index, name='index'),
    path('showdates', views.showdates, name='showdates'),
    path('photos', views.photos, name='photos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)