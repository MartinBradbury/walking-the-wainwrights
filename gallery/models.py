from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth.models import User
from routes.models import Comment, Route
from django.template.defaultfilters import slugify

STATUS = ((0, "Draft"), (1, "Published"))

class Gallery(models.Model):
    user_img = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    flagged = models.BooleanField(default=False)
    img_detail = models.TextField(max_length=50)
    likes = models.ManyToManyField(
        User, related_name='image_like', blank=True)

    class Meta:
        ordering = ["-uploaded_at"]
    def __str__(self):
        return self.title
    def number_of_likes(self):
        return self.likes.count()
    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        super(Gallery, self).save(*args, **kwargs)
        
class Comment(models.Model):
    post = models.ForeignKey(Gallery, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="gallery_comments"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)
    feature_img = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.id} by {self.author}"
