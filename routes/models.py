from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.html import format_html
from django.template.defaultfilters import slugify

STATUS = ((0, "Draft"), (1, "Published"))
DIFFICULTY_RATING = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]


class Route(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="route_posts"
    )
    content = models.TextField()
    os_url = models.URLField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post_edit = models.DateTimeField(auto_now=True)
    difficulty_rating = models.IntegerField(
        choices=DIFFICULTY_RATING,
        default=1
    )
    likes = models.ManyToManyField(
        User, related_name='blogpost_likes', blank=True
    )
    status = models.IntegerField(choices=STATUS, default=0)
    flagged = models.BooleanField(default=False)
    feature_img = CloudinaryField('image', default='placeholder')
    route_video = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:100]

    def number_of_likes(self):
        return self.likes.count()

    def difficulty_icon(self):
        icon_class = 'fa-solid fa-shoe-prints'
        icons_html = ''.join([
            f'<i class="fas {icon_class}"></i> | '
            for _ in range(self.difficulty_rating)
        ])

        return format_html(icons_html)


class Comment(models.Model):
    post = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)
    feature_img = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.id} by {self.author}"
