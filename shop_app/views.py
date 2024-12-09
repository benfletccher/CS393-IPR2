from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Cadet, Product, Customer, Vendor, Listing
from .forms import ProductLookup, CreateCustomerAccount, CreateVendorAccount, Login, newListing
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone



# Create your views here.

def logout_view(request):
    logout(request)
    return render(request, "shop_app/landing.html")

def landing(request):
    return render(request, "shop_app/landing.html")

def index(request):
    if request.method == "POST":
        submittedForm = Login(request.POST)
        if submittedForm.is_valid():
            user = authenticate(username=submittedForm.cleaned_data['username'], password=submittedForm.cleaned_data['password'])
            if user is not None:
                userType = submittedForm.cleaned_data['group']
                print(userType)
                login(request, user)
                if userType == "1":
                    return redirect("/vendor_landing")
                elif userType == "2": 
                    tempReq = request
                    return redirect("/customer_landing")
                else:
                    return Http404
            else:
                return redirect("/index")
    newForm = Login()
    context = {'login_form': newForm}
    return render(request, "shop_app/index.html", context)


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

def listing(request, listing_id):
    return HttpResponse(f"You're looking at task {listing_id}.")

@login_required
def customer_landing(request):
    listings = Listing.objects.order_by("listingdate")
    customer_name = request.user.first_name
    context = {"all_listings": listings, "customer_name":customer_name}
    return render(request, "shop_app/customer_landing.html", context)


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

@login_required
def vendor_landing(request):
    listings = Listing.objects.order_by("listingdate")
    customer_name = request.user.first_name
    context = {"all_listings": listings, "customer_name":customer_name}
    return render(request, "shop_app/vendor_landing.html", context)

def customer_create(request):
    newCustomer = None
    if request.method == "POST":
        form = CreateCustomerAccount(request.POST)
        if form.is_valid():
            try:
                customerUser = User.objects.get(username=form.cleaned_data['username'])
                return HttpResponse("User already exists")
            except User.DoesNotExist:
                customerUser = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                customerUser.first_name = form.cleaned_data['firstName']
                customerUser.last_name = form.cleaned_data['lastName']
                customerGroup = Group.objects.get(name='Customer')
                customerUser.groups.add(customerGroup)
                customerUser.save()
                ##print("GOT THROUGH USER CREATION")


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
                shoppingpreference = form.cleaned_data['shoppingPref'],
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

            try:
                vendorUser = User.objects.get(username=form.cleaned_data['username'])
                return HttpResponse("User already exists")
            except User.DoesNotExist:
                vendorUser = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                vendorUser.first_name = form.cleaned_data['firstName']
                vendorUser.last_name = form.cleaned_data['lastName']
                vendorGroup = Group.objects.get(name='Vendor')
                vendorUser.groups.add(vendorGroup)
                vendorUser.save()

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

@login_required
def new_listing(request):
    listing = None
    if request.method == "POST":
        form = newListing(request.POST)
        if form.is_valid():
            vendor_last = request.user.last_name
            vendor = Vendor.objects.select_related('cadet').filter(cadet__lastname=vendor_last).first()

            listing = Listing(
                vendorid = vendor,
                listingname = form.cleaned_data['listingName'],
                price = form.cleaned_data['price'],
                quantity = form.cleaned_data['quantity'],
                listingdate = timezone.now().date()
            )
            listing.save()
    newForm = newListing()
    context = {"create_listing":newForm}
    return render(request, 'shop_app/add_listing.html', context)