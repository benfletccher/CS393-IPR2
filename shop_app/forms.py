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