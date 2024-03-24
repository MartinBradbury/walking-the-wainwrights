from django.urls import path
from . import views
from .views import GalleryView, GalleryDetail

app_name = 'gallery'

urlpatterns = [
    path('', GalleryView.as_view(), name='gallery'),
    path('<slug:slug>/', GalleryDetail.as_view(), name='gallery_detail'),
    
]