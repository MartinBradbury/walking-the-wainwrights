from django.db import models
from cloudinary.models import CloudinaryField

COMPLETED = ((0, "Not Complete"), (1, "Completed"))

class About(models.Model):
    title = models.CharField(max_length=100)
    profile_img = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Wainwright(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    wainwright_img = CloudinaryField('image', default='placeholder')
    completed = models.IntegerField(choices=COMPLETED, default=0)

    def __str__(self):
        return self.name

class Carousel(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    img_1 = CloudinaryField('image', default='placeholder')
    img_2 = CloudinaryField('image', default='placeholder')
    img_3 = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title