from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.postgres.search import TrigramWordSimilarity
from .models import App, Ranking


import pandas as pd

df = pd.read_csv('data/app_all.csv', index_col='AppID', keep_default_na=False) # Null columns do not default to NaN

def jaccard_similarity(base_case, compartor):
	#convert strings to sets
	base_case = set(base_case.split(','))
	compartor = set(compartor.split(','))

	intersect = len(base_case & compartor)
	union = len(base_case | compartor)

	if union == 0: # do not divide by 0 check
		return 0
	else:
		return float(intersect) / float(union)

def find_similar(appID, comparing_column):
	k = 7 # 1 record will be removed by dropping appID record later

	base_record = df.loc[appID][comparing_column]

	# create a jaccard column that will hold the mapped similarity value of x compared to the base case appID
	df['Jaccard'] = df[comparing_column].map(lambda x: jaccard_similarity(base_record, x))

	similar_records = df.sort_values(by=['Jaccard'], ascending=False).head(k)

	return similar_records.drop([appID], axis=0)


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
        games = App.objects.all().order_by("AppID")
        
    paginator = Paginator(games, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'games': games,
        'query': query,
        'page_obj': page_obj
    }
    
    return render(request, 'gallery.html', context)
    



def gamedetail(request, AppID, comparing_column='Categories'):
    game = get_object_or_404(App, AppID=AppID)
    similar_games = find_similar(AppID, comparing_column)
    rankings = Ranking.objects.filter(App=AppID).order_by('-Date')
    page = request.GET.get('page', 1)
    
    context = {
        'game': game,
        'rankings': rankings,
        'similar_games': similar_games,
        'page': page,
    }
    
    return render(request, 'detail.html', context)