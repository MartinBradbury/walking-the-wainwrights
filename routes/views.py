from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from .models import Route
from .forms import CommentForm
from django.http import HttpResponseRedirect

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
        comments = route.comments.filter(approved=True).order_by("-created_on")
        comment_count = route.comments.filter(approved=True).count()

        return render(request, 'routes/routes_detail.html', 
        {
            'route': route,
            'comments': comments,
            "commented": False,
            'comment_count':comment_count,
            'comment_form':CommentForm(),
            },
        )

    def post(self, request, slug):
        route = get_object_or_404(Route, slug=slug)
        comments = route.comments.filter(approved=True).order_by("-created_on")
        comment_count = route.comments.filter(approved=True).count()
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user 
            comment.post = route
            comment.save()
        else:
            comment_form = CommentForm()

        return render(request, 'routes/routes_detail.html', 
        {
            'route': route,
            'comments': comments,
            "commented": True,
            'comment_count': comment_count,
            'comment_form': CommentForm(),
        })


class PostLike(View):
    def post(self, request, slug):
        route = get_object_or_404(Route, slug=slug)

        if route.likes.filter(id=request.user.id).exists():
            route.likes.remove(request.user)
        else:
            route.likes.add(request.user)
        return HttpResponseRedirect(reverse('routes:routes_detail', args=[slug]))