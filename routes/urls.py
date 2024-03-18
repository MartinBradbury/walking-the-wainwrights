from django.urls import path
from . import views


app_name = 'routes'

urlpatterns = [
    path('', views.routes, name='routes'),
    path('<slug:slug>/', views.routes_detail, name="detail"),
]

