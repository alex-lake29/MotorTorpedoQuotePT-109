from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    response = render(request, 'QuotePT109/index.html')
    return response

def generator(request):
    response = render(request, 'QuotePT109/generator.html')
    return response

def login(request):
    response = render(request, 'QuotePT109/login.html')
    return response

def login(request):
    response = render(request, 'QuotePT109/about.html')
    return response

def login(request):
    response = render(request, 'QuotePT109/generated.html')
    return response

# Create your views here.
