from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Cadet, Product, Customer, Vendor
from .forms import ProductLookup, CreateCustomerAccount, CreateVendorAccount



# Create your views here.

def landing(request):
    return render(request, "shop_app/landing.html")

def index(request):
    return render(request, "shop_app/index.html")


# View to display all of the cadets who have registered an account
# on the WP online trading post
def cadet_list(request):
    data = Cadet.objects.all()
    context = {'cadets': data}
    return render(request, "shop_app/cadet_list.html", context)

def product_list(request):
    data = Product.objects.all()
    context = {'products': data}
    return render(request, "shop_app/product_list.html", context)

def product_lookup(request):
    products=None
    if request.method == "GET":
        empty_form = ProductLookup()
        context = {'form':empty_form}
        return render(request, "shop_app/product_lookup.html", context)
    if request.method == "POST":
        submittedForm = ProductLookup(request.POST)
        if submittedForm.is_valid():
            productName = submittedForm.cleaned_data['prodName']
            products = Product.objects.filter(prodname__contains=productName)
    context = {'products':products}
    return render(request, 'shop_app/product_results.html', context)

def customer_create(request):
    newCustomer = None
    if request.method == "POST":
        form = CreateCustomerAccount(request.POST)
        if form.is_valid():
            newCadet = Cadet(
                cadetid = form.cleaned_data['cadetId'],
                firstname = form.cleaned_data['firstName'],
                lastname = form.cleaned_data['lastName'],
                company = form.cleaned_data['company'],
                gradyear = form.cleaned_data['gradYear'],
                roomnumber = form.cleaned_data['roomNum'],
                email = form.cleaned_data['email'],
                venmo = form.cleaned_data['venmo'],
            )
            newCadet.save()
            toAddCadet = Cadet.objects.get(cadetid = form.cleaned_data['cadetId'])
            newCustomer = Customer(
                cadet = toAddCadet,
                shoppingpreference = form.cleaned_data['shoppingPref']
            )
            newCustomer.save()
    newForm = CreateCustomerAccount()
    context = {'customer_create_form':newForm}
    return render(request, 'shop_app/customer_create.html', context)

def vendor_create(request):
    newVendor = None
    if request.method == "POST":
        form = CreateVendorAccount(request.POST)
        if form.is_valid():
            newCadet = Cadet(
                cadetid = form.cleaned_data['cadetId'],
                firstname = form.cleaned_data['firstName'],
                lastname = form.cleaned_data['lastName'],
                company = form.cleaned_data['company'],
                gradyear = form.cleaned_data['gradYear'],
                roomnumber = form.cleaned_data['roomNum'],
                email = form.cleaned_data['email'],
                venmo = form.cleaned_data['venmo'],
            )
            newCadet.save()
            toAddCadet = Cadet.objects.get(cadetid = form.cleaned_data['cadetId'])
            newVendor = Vendor(
                cadet = toAddCadet,
                dodid = form.cleaned_data['dodId']
            )
            newVendor.save()
    newForm = CreateVendorAccount()
    context = {'vendor_create_form':newForm}
    return render(request, 'shop_app/vendor_create.html', context)
