from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Route
from .forms import CommentForm

class Routes(View):
    def get(self, request):
        route_list = Route.objects.filter(status=1) # Filter routes with status 1
        paginator = Paginator(route_list, 4)
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'routes/routes.html', {'page_object': page_object})

class RoutesDetail(View):
    def get(self, request, slug):
        route = get_object_or_404(Route, slug=slug)
        comments = route.comments.all()
        comment_count = route.comments.filter(approved=True).count()

        return render(request, 'routes/routes_detail.html', 
        {
            'route': route,
            'comments': comments,
            'comment_count':comment_count,
            'comment_form':CommentForm(),
            },
        )

