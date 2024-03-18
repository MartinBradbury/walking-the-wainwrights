from django.shortcuts import render
from .models import Route

# Create your views here.



def routes(request):
    route = Route.objects.all()
    return render(request, 'routes.html', {'route':route},)

def routes_detail(request, slug):
    # return HttpResponse(slug)
    route = Route.objects.get(slug=slug)
    return render(request, 'routes_detail.html', {'route':route})