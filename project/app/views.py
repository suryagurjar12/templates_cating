from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def cars(request):
    return render(request,'cars.html')

def Services(request):
    return render(request,'Services.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
