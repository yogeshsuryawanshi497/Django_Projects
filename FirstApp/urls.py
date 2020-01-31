from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('dynamic_home', views.dynamic_home, name='dynamic_home')

]