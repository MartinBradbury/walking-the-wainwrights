from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def routes (request):
#     return HttpResponse("Testing")



def routes(request):
    return render(request, 'routes.html')