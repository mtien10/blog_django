from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/home.html')
def info(request):
    return render(request, 'pages/info.html') 
def contact(request):
    return render(request, 'pages/contact.html')