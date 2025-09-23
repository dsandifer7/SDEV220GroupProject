
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('add/', views.add_url, name='add_url'),
    path('delete/<int:pk>/', views.delete_url, name='delete_url'),
    path('library/', views.url_library, name='url_library'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)