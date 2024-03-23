from django.shortcuts import render
from .models import About
from django.views import View


class AboutView(View):
    def get(self, request):
        about = About.objects.first() # Corrected line

        return render(request, 'about/about.html', 
        {
            'about': about,
            },
        )
