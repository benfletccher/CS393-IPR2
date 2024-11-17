from django.shortcuts import render
from django.http import HttpResponse
#from .forms import Hours
#^^ update for this repos folder
#from .models import HoursLogged
##^^ update for this repos folder


# Create your views here.

def index(request):
    return HttpResponse('Welcome to the Cadet ONline Trading Post')