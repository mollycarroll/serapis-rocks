from django.db import models

class HomeText(models.Model):
    text = models.TextField()

class Show(models.Model):
    class Meta:
        ordering = ['-show_date']

    def __str__(self):
        return str(self.show_date)

    venue = models.CharField(max_length=100)
    show_date = models.DateTimeField()
    city = models.CharField(max_length=100)


class LatestVideo(models.Model):
    url = models.CharField(max_length=200, blank=True)


class Musician(models.Model):
    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='member_photos')


class Photo(models.Model):
    def __str__(self):
        return str(self.caption)

    upload = models.ImageField(upload_to='band_photos')
    caption = models.CharField(max_length=200)


class Video(models.Model):
    def __str__(self):
        return str(self.title)

    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)