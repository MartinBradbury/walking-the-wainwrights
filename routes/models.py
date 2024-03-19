from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

class Route(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="route_post"
    )
    content = models.TextField()
    os_url = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)
    post_edit = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    flagged = models.BooleanField()
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return self.title
    def snippet(self):
        return self.content[:50]

class Comment(models.Model):
    post = models.ForeignKey(Route, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.id} by {self.author}"