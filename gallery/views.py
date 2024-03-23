from django.shortcuts import render

def gallery_view(request):
    return render(request, 'gallery/gallery.html')