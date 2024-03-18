from django.shortcuts import render
from .models import Route

# Create your views here.



def routes(request):

    route = Route.objects.all()
    return render(request, 'routes.html', {'route':route},)