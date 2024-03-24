from django.urls import path
from . import views
from .views import GalleryView, GalleryDetail

app_name = 'gallery'

urlpatterns = [
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('', GalleryView.as_view(), name='gallery'),
    path('<slug:slug>/', GalleryDetail.as_view(), name='gallery_detail'),
    path('<slug:slug>', views.PostLike.as_view(), name='post-like'),
    
]