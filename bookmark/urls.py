''' import django authentication views '''
# from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'bookmark'

urlpatterns = [
    
    # start authetication path 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),
    
    # signup url 
    path('signup/', views.SignupPageView.as_view(), name='signup'),
    
    path('password_change/', auth_views.LoginView.as_view(), name='password_change'),
    path('password_change/done/',auth_views.LoginView.as_view(), name='password_change_done'),
    path('password_reset/',auth_views.LoginView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.LoginView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.LoginView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.LoginView.as_view(), name='password_reset_complete'),
    # end authentication path 
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('form_done/', views.form_done, name='form_done'),
    path('info/', views.info, name='info'),
]
