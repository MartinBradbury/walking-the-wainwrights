from .models import Comment, Gallery
from django import forms
from cloudinary.forms import CloudinaryFileField

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)