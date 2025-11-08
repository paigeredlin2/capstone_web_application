from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import App, Ranking

class AppResource(resources.ModelResource):
    class Meta:
        model = App
        import_id_fields = ['AppID']
        fields = ('AppID', 'Name', 'Description', 'Type', 'Required_Age', 'Recommendations', 'Is_Free', 'Discount_Percent', 'Price', 'Coming_Soon', 'Release_Date', 'Full_AppID', 'Image_Link')

class RankingResource(resources.ModelResource):
    App = fields.Field(
        column_name='AppID',        
        attribute='App',             
        widget=ForeignKeyWidget(App, 'AppID') 
    )

    class Meta:
        model = Ranking

        