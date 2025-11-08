from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import App, Ranking
from .resources import AppResource, RankingResource

# Register your models here.
@admin.register(App)
class AppAdmin(ImportExportModelAdmin):
    resource_class = AppResource
    list_display = ('Name', 'Release_Date')
    search_fields = ('AppID', 'Name')

@admin.register(Ranking)
class RankingAdmin(ImportExportModelAdmin):
    resource_class = RankingResource
    list_display = ('App', 'Date', 'Rank', 'Player_Count')
    search_fields = ('App', 'Date', 'Rank')