from django.urls import path
from Sign_up import views

urlpatterns = [
    path("",views.login, name='login'),
    path("signup/", views.signup, name='signup'),
]