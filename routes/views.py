from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Route

def routes(request):
    route_list = Route.objects.filter(status=1) # Filter routes with status 1
    paginator = Paginator(route_list, 4)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'routes/routes.html', {'page_object': page_object})


def routes_detail(request, slug):
    route = get_object_or_404(Route, slug=slug)
    return render(request, 'routes/routes_detail.html', {'route':route})