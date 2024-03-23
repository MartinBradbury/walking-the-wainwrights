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