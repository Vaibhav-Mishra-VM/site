from django.db import models 
from django_mysql.models import ListCharField

# Create your models here.
class Movie(models.Model):
    mov_name = models.CharField(max_length=250)
    mov_desc = models.TextField()
    mov_cat = ListCharField(
        base_field=models.CharField(max_length=20),
        size=3,
        max_length=(6 * 20),  # 6 * 10 character nominals, plus commas
    )
    mov_trailer = models.TextField()
    mov_img = models.ImageField(upload_to='images', default="")
    mov_poster = models.ImageField(upload_to='posters', default="")
    mov_vid = models.FileField(upload_to='vid')
    def __str__(self):
        return self.mov_name
    
class Series(models.Model):
    ser_name = models.CharField(max_length=250)
    ser_desc = models.TextField()
    ser_cat = ListCharField(
        base_field=models.CharField(max_length=20),
        size=3,
        max_length=(6 * 20),  # 6 * 10 character nominals, plus commas
    )
    ser_trailer = models.TextField()
    ser_img = models.ImageField(upload_to='images', default="")
    ser_poster = models.ImageField(upload_to='posters', default="")
    ser_vid = models.FileField(upload_to='servid')
    def __str__(self):
        return self.ser_name
