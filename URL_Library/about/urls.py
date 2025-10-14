from django.urls import path
from . import views  

app_name = 'about' 

urlpatterns = [
    path('', views.about_view, name='how_it_works'),  
]
