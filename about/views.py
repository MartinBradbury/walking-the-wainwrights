from django.shortcuts import render
from .models import About, Wainwright
from django.views import View


class AboutView(View):
    def get(self, request):
        about = About.objects.first() # Corrected line

        return render(request, 'about/about.html', 
        {
            'about': about,
            },
        )

def wainwrights(request):
    wainwrights = Wainwright.objects.filter(completed=1)
    return render(request, 'about/wainwrights.html', {'wainwrights': wainwrights})

def contact(request):
    return render(request, 'contact/contact.html',)