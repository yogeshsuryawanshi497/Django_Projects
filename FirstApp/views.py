from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def dynamic_home(request):
    return render(request, 'dynamic_home.html', {'name': 'Ankit Sharma', 'Age': 23})

def login(request):
    return render(request, 'login.html')
