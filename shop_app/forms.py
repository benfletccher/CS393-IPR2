from django import forms

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

class newListing(forms.Form):
    listingName = forms.CharField(label="Listing Name", max_length=255)
    price = forms.DecimalField(label="Price", max_digits=6, decimal_places=2)
    quantity = forms.IntegerField(label="Quantity")
    #listingDate = forms.DateField(label="Today's Date (YYYY-MM-DD)")

GROUP_CHOICES = (
    ("1", "Vendor"),
    ("2", "Customer"),
)

class Login(forms.Form):
    username = forms.CharField(label="Username", max_length=50, min_length=1)
    password = forms.CharField(widget=forms.PasswordInput)
    group = forms.ChoiceField(choices=GROUP_CHOICES)