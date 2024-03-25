from django.shortcuts import render
from .models import About, Wainwright, Carousel
from django.views import View


class AboutView(View):
    def get(self, request):
        about = About.objects.first() # Corrected line
        carousel = Carousel.objects.all()[0]
        return render(request, 'about/about.html', 
        {
            'about': about,
            'carousel': carousel,
            },
        )

def wainwrights(request):
    wainwrights = Wainwright.objects.filter(completed=1)
    return render(request, 'about/wainwrights.html', {'wainwrights': wainwrights})

def contact(request):
    return render(request, 'contact/contact.html',)