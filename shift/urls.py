from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('start', views.user_start_shift, name='user_start_shift'),
    path('end', views.user_end_shift, name='user_end_shift'),
]