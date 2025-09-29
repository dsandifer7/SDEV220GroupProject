from django.urls import path
from Main import views

urlpatterns = [
    path("",views.url_library, name='url_library'),
    path("add/",views.add_url, name='url_library'),
    #path("delete/",views.delete_url, name='url_library'),
]