from django.db import models

# Create your models here.

class APPS(models.Model):
    AppID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=300)
    Description = models.TextField(max_length=500, null=True)
    Type = models.CharField(max_length=20)
    Required_Age = models.IntegerField(null=True)
    Recommendations = models.IntegerField(null=True)
    Is_Free = models.BooleanField()
    Discount_Percent = models.IntegerField(null=True)
    Price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    Coming_Soon = models.BooleanField()
    Release_Date = models.DateField(null=True)
    Full_AppID = models.IntegerField(null=True)
    Image_Link = models.CharField(max_length=200, null=True)

class CATEGORIES(models.Model):
    CategoryID = models.IntegerField(primary_key=True)
    Description = models.CharField(max_length=50)

class GENRES(models.Model):
    GenreID = models.IntegerField(primary_key=True)
    Description = models.CharField(max_length=50)

class DEVELOPERS(models.Model):
    DeveloperID = models.IntegerField(primary_key=True)
    Developer_Name = models.CharField(max_length=100)

class PUBLISHERS(models.Model):
    PublisherID = models.IntegerField(primary_key=True)
    Publisher_Name = models.CharField(max_length=100)

class LANGUAGES(models.Model):
    LanguageID = models.IntegerField(primary_key=True)
    Language = models.CharField(max_length=100)

class APP_CATEGORIES(models.Model):
    pk = models.CompositePrimaryKey('AppID', 'CategoryID')
    AppID = models.ForeignKey('APPS', on_delete=models.PROTECT)
    CategoryID = models.ForeignKey('CATEGORIES', on_delete=models.PROTECT)

class APP_GENRES(models.Model):
    pk = models.CompositePrimaryKey('AppID', 'GenreID')
    AppID = models.ForeignKey('APPS', on_delete=models.PROTECT)
    GenreID = models.ForeignKey('GENRES', on_delete=models.PROTECT)

class APP_DEVELOPERS(models.Model):
    pk = models.CompositePrimaryKey('AppID', 'DeveloperID')
    AppID = models.ForeignKey('APPS', on_delete=models.PROTECT)
    DeveloperID = models.ForeignKey('DEVELOPERS', on_delete=models.PROTECT)

class APP_PUBLISHERS(models.Model):
    pk = models.CompositePrimaryKey('AppID', 'PublisherID')
    AppID = models.ForeignKey('APPS', on_delete=models.PROTECT)
    PublisherID = models.ForeignKey('PUBLISHERS', on_delete=models.PROTECT)

class APP_LANGUAGES(models.Model):
    pk = models.CompositePrimaryKey('AppID', 'LanguageID')
    AppID = models.ForeignKey('APPS', on_delete=models.PROTECT)
    LanguageID = models.ForeignKey('LANGUAGES', on_delete=models.PROTECT)
    Audio_Support = models.BooleanField()

class RANKINGS(models.Model):
    pk = models.CompositePrimaryKey('AppID', 'Date')
    AppID = models.ForeignKey('APPS', on_delete=models.PROTECT)
    Date = models.DateField()
    Rank = models.IntegerField()
    Player_Count = models.IntegerField(null=True)