from django.contrib import admin
from .models import Show, Musician, Photo, HomeText, LatestVideo

admin.site.register(Show)
admin.site.register(Musician)
admin.site.register(Photo)
admin.site.register(HomeText)
admin.site.register(LatestVideo)