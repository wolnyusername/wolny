from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('home', views.Home.as_view(), name='home'),
    path('home/start', views.UserStartShift.as_view(), name='user_start_shift'),
    path('home/end', views.UserEndShift.as_view(), name='user_end_shift'),
    path('home/logout', views.LogOut.as_view(), name='log_out')
]