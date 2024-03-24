from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from .models import Route, Comment, Gallery
from .forms import CommentForm
from django.http import HttpResponseRedirect


class GalleryView(View):
    def get(self, request):
        user_img = Gallery.objects.filter(status=1)
        paginator = Paginator(user_img, 4)
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'gallery/gallery.html', {'page_object': page_object})

class GalleryDetail(View):
    def get(self, request, slug):
        gallery = get_object_or_404(Gallery, slug=slug)
        print('slug')
        comments = gallery.comments.all().order_by("-created_on")
        comment_count = gallery.comments.filter(approved=True).count()
        liked = False
        if gallery.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(request, 'gallery/gallery_detail.html', 
        {
            'gallery': gallery,
            'comments': comments,
            "gallery_comments": False,
            "liked": liked,
            'comment_count':comment_count,
            'comment_form':CommentForm(),
            },
        )

    def post(self, request, slug):
        gallery = get_object_or_404(Gallery, slug=slug)
        comments = gallery.comments.all().order_by("-created_on")
        comment_count = gallery.comments.filter(approved=True).count()
        comment_form = CommentForm(data=request.POST)
        liked = False
        if gallery.likes.filter(id=self.request.user.id).exists():
            liked = True

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user 
            comment.post = gallery
            comment.save()
        else:
            comment_form = CommentForm()

        return render(request, 'gallery/gallery_detail.html', 
        {
            'gallery': gallery,
            'comments': comments,
            "gallery_comments": True,
            "liked": liked,
            'comment_count': comment_count,
            'comment_form': CommentForm(),
        })


class PostLike(View):
    def post(self, request, slug):
        gallery = get_object_or_404(Gallery, slug=slug)

        if gallery.likes.filter(id=request.user.id).exists():
            gallery.likes.remove(request.user)
        else:
            gallery.likes.add(request.user)
        return HttpResponseRedirect(reverse('gallery:gallery_detail', args=[slug]))