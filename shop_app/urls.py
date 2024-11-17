from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadet_list', views.cadet_list, name='cadets'),
    path('product_list', views.product_list, name='products')
]