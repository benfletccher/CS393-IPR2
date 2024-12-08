from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('index', views.index, name='index'),
    path('cadet_list', views.cadet_list, name='cadets'),
    path('product_list', views.product_list, name='products'),
    path('product_lookup/', views.product_lookup, name='product_lookup')
]