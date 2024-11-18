from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Cadet, Product
from .forms import ProductLookup



# Create your views here.

def index(request):
    return render(request, "shop_app/shop.html") #HttpResponse('Welcome to the Cadet Online Trading Post')


# View to display all of the cadets who have registered an account
# on the WP online trading post
def cadet_list(request):
    data = Cadet.objects.all()
    context = {'cadets': data}
    return render(request, "shop_app/cadet_list.html", context)

def product_list(request):
    data = Product.object.all()
    context = {'products': data}
    return render(request, "shop_app/product_list.html", context)

def product_lookup(request):
    if request.method == "POST":
        submittedForm = ProductLookup(request.POST)
        if submittedForm.is_valid():
            productName = submittedForm.cleaned_data['prodName']
            products = Product.objects.filter(prodname__contains=productName)
    context = {'Product':products}
    return render(request, 'shop_app/product_result.html', context)