from django.urls import path
from . import views
from .views import AboutView, wainwrights, contact

app_name = 'about'

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('wainwrights/', wainwrights, name='wainwrights'),
    path('contact/', contact, name='contact'),
    
]
