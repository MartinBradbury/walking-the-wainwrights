from .models import Comment, Gallery
from django import forms
from cloudinary.forms import CloudinaryFileField

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)

class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ['title', 'img_detail']