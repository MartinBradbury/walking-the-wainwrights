from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.

class Routes(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = models.TextField()
    os_url = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)
    post_edit = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    flagged = models.BooleanField()

    def __str__(self):
        return self.title
