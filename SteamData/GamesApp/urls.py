from django.urls import path
from . import views

urlpatterns = [
    path('gallery', views.gallery, name='gallery'),
    path('detail/<int:AppID>/', views.gamedetail, name='detail')
]