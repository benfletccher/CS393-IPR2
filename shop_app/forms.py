from django import forms
from .models import Cadet, Product

class addCadet(forms.Form):
    cadetId = forms.IntegerField(label="C-Num")
    firstName = forms.CharField(label="First Name", max_length=100, min_length=1)
    lastName = forms.CharField(label="Last Name", max_length=200, min_length=1)
    company = forms.CharField(label="Company", max_length=2, min_length=2)
    gradYear = forms.CharField(label="Graduation Year", max_length=4, min_length=4)
    roomNum = forms.IntegerField(label="Room Number", max_value=10, min_value=1)
    email = forms.EmailField(label= "Email", max_length=200)
    venmo = forms.CharField(label="Venmo Username", max_length=100)

class ProductLookup(forms.Form):
    prodName = forms.CharField(label="Product Name", max_length=255)

class CreateCustomerAccount(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    cadetId = forms.IntegerField(label="C-Num")
    firstName = forms.CharField(label="First Name", max_length=100, min_length=1)
    lastName = forms.CharField(label="Last Name", max_length=200, min_length=1)
    company = forms.CharField(label="Company", max_length=2, min_length=2)
    gradYear = forms.CharField(label="Graduation Year", max_length=4, min_length=4)
    roomNum = forms.IntegerField(label="Room Number", min_value=1)
    email = forms.EmailField(label= "Email", max_length=200)
    venmo = forms.CharField(label="Venmo Username", max_length=100)
    shoppingPref = forms.CharField(label="Shopping Preferences ('Clothes' or 'Other')", max_length=255)

class CreateVendorAccount(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    cadetId = forms.IntegerField(label="C-Num")
    firstName = forms.CharField(label="First Name", max_length=100, min_length=1)
    lastName = forms.CharField(label="Last Name", max_length=200, min_length=1)
    company = forms.CharField(label="Company", max_length=2, min_length=2)
    gradYear = forms.CharField(label="Graduation Year", max_length=4, min_length=4)
    roomNum = forms.IntegerField(label="Room Number", min_value=1)
    email = forms.EmailField(label= "Email", max_length=200)
    venmo = forms.CharField(label="Venmo Username", max_length=100)
    dodId = forms.IntegerField(label='DOD ID')

PRODUCT_CHOICES = (
    (1, "Bathrobe"),
    (2, "Chest"),
    (3, "ACU Blouse"),
    (4, "ACU Trouser"),
    (5, "Monitor"),
    (6, "APFU Shirt"),
    (7, "APFU Shorts"),
    (8, "APFU Jacket"),
    (9, "APFU Pants"),
    (10, "AFC Shirt"),
    (11, "LSAFC Shirt"),
    (12, "Gray Trousers"),
    (13, "White Trousers"),
    (14, "Summer ACU Blouse"),
    (15, "Summer ACU Trouser"),
    (16, "Combination Lock"),
    (17, "Low Quarters"),
    (18, "Shoe Shine"),
    (19, "White Socks"),
    (20, "Black Socks"),
)

class newListing(forms.Form):
    # create dropdown with all products to select choices
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label="Product")
    listingName = forms.CharField(label="Listing Name", max_length=255)
    price = forms.DecimalField(label="Price", max_digits=6, decimal_places=2)
    quantity = forms.IntegerField(label="Quantity")

GROUP_CHOICES = (
    ("1", "Vendor"),
    ("2", "Customer"),
)

class Login(forms.Form):
    username = forms.CharField(label="Username", max_length=50, min_length=1)
    password = forms.CharField(widget=forms.PasswordInput)
    group = forms.ChoiceField(choices=GROUP_CHOICES)