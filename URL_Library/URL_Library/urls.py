"""
URL configuration for URLlibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Main import views as main_views
from Sign_up import views as signup_views
# define paths for all pages
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', main_views.add_url, name='add_url'),
    #path('delete/', views.delete_url, name='delete_url'),
    path('library/', main_views.url_library, name='url_library'),
    path('login/', signup_views.login, name='login'),
    path('signup/', signup_views.signup, name='signup'),
]
## define path for qr images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
