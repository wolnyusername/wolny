from django.urls import path

from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('home', views.HomeView.as_view(), name='home'),
    path('home/start', views.UserStartShiftView.as_view(), name='user_start_shift'),
    path('home/end', views.UserEndShiftView.as_view(), name='user_end_shift'),
    path('home/logout', views.LogOutView.as_view(), name='log_out')
]