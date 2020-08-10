from . import views
from django.urls import path,include

urlpatterns = [
   # path('index/', views.index,name='index'),
    path('register/#',views.register,name='register'),
    path('login/#',views.login,name='login'),
    path('logout/#',views.logout,name='logout'),
]
   
