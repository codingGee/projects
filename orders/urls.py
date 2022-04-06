from django import views
from django.urls import path
from . import views 

app_name = 'orders'

urlpatterns = [
    path('charge/',views.charge, name='charge'),
    path('', views.OrdersPageView.as_view(), name='orders'),
   
]