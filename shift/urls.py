from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('home/start', views.user_start_shift, name='user_start_shift'),
    path('home/end', views.user_end_shift, name='user_end_shift'),
    path('home/logout', views.log_out, name='log_out')
]