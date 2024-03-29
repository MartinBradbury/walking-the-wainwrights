from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from .models import Route, Comment
from .forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect


class Routes(View):
    def get(self, request):
        route_list = Route.objects.filter(status=1)
        paginator = Paginator(route_list, 4)
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(
            request, 'routes/routes.html', {'page_object': page_object}
        )


class RoutesDetail(View):
    def get(self, request, slug):
        route = get_object_or_404(Route, slug=slug)
        comments = route.comments.all().order_by("-created_on")
        comment_count = route.comments.filter(approved=True).count()
        liked = False
        if route.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 'routes/routes_detail.html',
            {
                'route': route,
                'comments': comments,
                "commented": False,
                "liked": liked,
                'comment_count': comment_count,
                'comment_form': CommentForm(),
            }
        )

    def post(self, request, slug):
        route = get_object_or_404(Route, slug=slug)
        comments = route.comments.all().order_by("-created_on")
        comment_count = route.comments.filter(approved=True).count()
        comment_form = CommentForm(data=request.POST)
        liked = False
        if route.likes.filter(id=self.request.user.id).exists():
            liked = True

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = route
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request, 'routes/routes_detail.html',
            {
                'route': route,
                'comments': comments,
                "commented": True,
                "liked": liked,
                'comment_count': comment_count,
                'comment_form': CommentForm(),
            }
        )


class PostLike(View):
    def post(self, request, slug):
        route = get_object_or_404(Route, slug=slug)

        if route.likes.filter(id=request.user.id).exists():
            route.likes.remove(request.user)
        else:
            route.likes.add(request.user)
        return HttpResponseRedirect(
            reverse('routes:routes_detail', args=[slug])
        )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Route.objects.filter(status=1)
        route = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = route
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('routes:routes_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Route.objects.filter(status=1)
    route = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('routes:routes_detail', args=[slug]))
