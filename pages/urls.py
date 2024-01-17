from django.urls import path #import the path function from django.urls
from .views import HomePageView #import the homePageView function from views.py
urlpatterns = [
    #for class based views, we need to use the as_view() method
    path('', HomePageView.as_view(), name='home') 
]