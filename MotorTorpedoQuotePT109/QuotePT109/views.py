from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    response = render(request, 'QuotePT109/index.html')
    return response
    return HttpResponse("Motor Torpedo Quote PT-109")


# Create your views here.
