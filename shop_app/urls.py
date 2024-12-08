from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('index', views.index, name='index'),
    path('logout', views.logout_view, name='logout'),
    path('cadet_list', views.cadet_list, name='cadets'),
    path('product_list', views.product_list, name='products'),
    path('product_lookup/', views.product_lookup, name='product_lookup'),
    path('vendor_create', views.vendor_create, name='vendor_create'),
    path('customer_create', views.customer_create, name='customer_create'),
    path("customer_landing", views.customer_landing, name='all_listings')
]