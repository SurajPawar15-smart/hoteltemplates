from django.urls import path
from .  import views

urlpatterns = [
   path('contact/', views.contact,name='contact'),
   path('/home/', views.home,name='home'),
   path('', views.index,name='index'),
   path('about/', views.about,name='about'),
   path('news/', views.news,name='news'),
   path('elements/', views.elements,name='elements'),
   path('destinations/', views.destinations,name='destinations'),
    
    
    ]
