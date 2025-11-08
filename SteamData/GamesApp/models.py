from django.db import models

# Create your models here.

class App(models.Model):
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

    def __str__(self):
        return self.Name

class Ranking(models.Model):
    App = models.ForeignKey(App, on_delete=models.CASCADE)
    Date = models.DateField()
    Rank = models.IntegerField()
    Player_Count = models.IntegerField(null=True)

    def __str__(self):
        return (f'{self.App}, {self.Date}')