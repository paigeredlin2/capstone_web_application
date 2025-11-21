from django.shortcuts import render, HttpResponse
from GamesApp.models import App

# Create your views here.
def home(request):
    featured_apps = App.objects.all()[:5]
    context = {
        'featured_apps' : featured_apps
    }
    return render(request, 'home.html', context)

def documentation(request):
    return render(request, 'documentation.html')

def about(request):
    return render(request, 'about.html')
