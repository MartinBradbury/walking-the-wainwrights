from django.urls import path
from .views import Routes, RoutesDetail, PostLike
from . import views

app_name = 'routes'

urlpatterns = [
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('', Routes.as_view(), name='routes'),
    path('<slug:slug>/', RoutesDetail.as_view(), name='routes_detail'),
    path('<slug:slug>', views.PostLike.as_view(), name='post-like'),
    
]
