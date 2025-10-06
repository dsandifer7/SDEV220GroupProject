from django.urls import path
from Main import views

urlpatterns = [
    path("", views.url_library, name='url_library'),
    path('my_library', views.myurls_library, name='myurls_library'),
    #path("delete <int:pk>",views.delete_url, name='url_library'),
]