from django.shortcuts import render

def home(request):
    return render(request, 'solar/index.html')

def residential_solar(request):
    return render(request, 'solar/residential_solar.html')

def commercial_solar(request):
    return render(request, 'solar/commercial_solar.html')