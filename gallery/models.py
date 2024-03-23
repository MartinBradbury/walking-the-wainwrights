from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from routes.models import Comment, Route

STATUS = ((0, "Draft"), (1, "Published"))

class Gallery(models.Model):
    user_img = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    flagged = models.BooleanField()

    def __str__(self):
        return self.title
