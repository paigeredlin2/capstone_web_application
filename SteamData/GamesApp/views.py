from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import App, Ranking

# Create your views here.
def gallery(request):
    games = App.objects.all()
    paginator = Paginator(games, 21)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery.html', {'page_obj': page_obj})

def gamedetail(request, AppID):
    game = get_object_or_404(App, AppID=AppID)
    return render(request, 'detail.html', {'game': game})