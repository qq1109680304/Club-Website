from django.shortcuts import render
from .models import AboutPage

def about_page(request):
    about = AboutPage.objects.all()
    context = {'about': about}
    return render(request, 'about/about.html', context)