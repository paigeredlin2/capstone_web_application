from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.postgres.search import TrigramWordSimilarity
from .models import App, Ranking

# Create your views here.
def gallery(request):
    query = request.GET.get('q', '')
    
    if query:
        games = App.objects.annotate(
            similarity=TrigramWordSimilarity(query, "Name"),
            ).filter(
                similarity__gt=0.4
            ).order_by("-similarity")    
    else: 
        games = App.objects.all()
        
    paginator = Paginator(games, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'games': games,
        'query': query,
        'page_obj': page_obj
    }
    
    return render(request, 'gallery.html', context)
    

def gamedetail(request, AppID):
    game = get_object_or_404(App, AppID=AppID)
    rankings = Ranking.objects.filter(App=AppID).order_by('-Date')
    page = request.GET.get('page', 1)
    
    context = {
        'game': game,
        'rankings': rankings,
        'page': page,
    }
    
    return render(request, 'detail.html', context)