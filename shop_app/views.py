from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
#from .forms import Hours
#^^ update for this repos folder
#from .models import HoursLogged
##^^ update for this repos folder


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