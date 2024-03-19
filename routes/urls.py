from django.urls import path
from .views import Routes, RoutesDetail

app_name = 'routes'

urlpatterns = [
    path('', Routes.as_view(), name='routes'),
    path('routes/<slug:slug>/', RoutesDetail.as_view(), name='routes_detail'),
]
