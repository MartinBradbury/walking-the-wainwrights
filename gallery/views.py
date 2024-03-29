from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.contrib import messages

from .models import Gallery, Comment
from .forms import CommentForm, GalleryForm


class GalleryView(View):
    def get(self, request):
        feature_img = Gallery.objects.filter(status=1)
        paginator = Paginator(feature_img, 4)
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        gallery_form = GalleryForm()
        return render(request, 'gallery/gallery.html', {
            'page_object': page_object,
            'gallery_form': gallery_form,
        })

    def post(self, request):
        gallery_form = GalleryForm(request.POST, request.FILES)
        if gallery_form.is_valid():
            gallery = gallery_form.save(commit=False)
            gallery.author = request.user
            gallery.feature_img = request.POST.get('feature_img')
            gallery.save()
            messages.success(request, 'Gallery uploaded successfully!')
            feature_img = Gallery.objects.filter(status=1)
            paginator = Paginator(feature_img, 4)
            page_number = request.GET.get('page')
            page_object = paginator.get_page(page_number)

            return render(request, 'gallery/gallery.html', {
                'page_object': page_object,
                'gallery_form': GalleryForm(),
            })
        else:
            messages.error(
                request, 'Error uploading gallery. Please try again.'
            )
            return render(request, 'gallery/gallery.html', {
                'page_object': page_object,
                'gallery_form': GalleryForm(),
            })


class GalleryDetail(View):
    def get(self, request, slug):
        gallery = self.get_gallery(slug)
        comments = gallery.comments.all().order_by("-created_on")
        comment_count = gallery.comments.filter(approved=True).count()
        liked = gallery.likes.filter(id=request.user.id).exists()

        return render(request, 'gallery/gallery_detail.html', {
            'gallery': gallery,
            'comments': comments,
            "gallery_comments": False,
            "liked": liked,
            'comment_count': comment_count,
            'comment_form': CommentForm(),
        })

    def post(self, request, slug):
        gallery = self.get_gallery(slug)
        comments = gallery.comments.all().order_by("-created_on")
        comment_count = gallery.comments.filter(approved=True).count()
        comment_form = CommentForm(data=request.POST)
        liked = gallery.likes.filter(id=request.user.id).exists()

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = gallery
            comment.feature_img = request.POST.get('feature_img')
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment submitted!'
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'Error submitting comment!'
            )

        return render(request, 'gallery/gallery_detail.html', {
            'gallery': gallery,
            'comments': comments,
            "gallery_comments": True,
            "liked": liked,
            'comment_count': comment_count,
            'comment_form': CommentForm(),
        })

    def get_gallery(self, slug):
        return get_object_or_404(Gallery, slug=slug)


class PostLike(View):
    def post(self, request, slug):
        gallery = get_object_or_404(Gallery, slug=slug)
        if gallery.likes.filter(id=request.user.id).exists():
            gallery.likes.remove(request.user)
        else:
            gallery.likes.add(request.user)
        return HttpResponseRedirect(
            reverse('gallery:gallery_detail', args=[slug])
        )


def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        gallery = get_object_or_404(
            Gallery.objects.filter(status=1), slug=slug
        )
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = gallery
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('gallery:gallery_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    gallery = get_object_or_404(Gallery.objects.filter(status=1), slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('gallery:gallery_detail', args=[slug]))
