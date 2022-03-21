from django.shortcuts import render
from django.http import HttpResponse
from QuotePT109.models import Category, Page
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-likes')[:5]
    context_dict={}
    context_dict['pages'] = page_list
    context_dict['categories'] = category_list
    return render(request, 'QuotePT109/index.html', context=context_dict)
    

def generator(request):
    response = render(request, 'QuotePT109/generator.html')
    return response

def login(request):
    response = render(request, 'QuotePT109/login.html')
    return response

def preGenerator(request):
    response = render(request, 'QuotePT109/preGenerate.html')
    return response

def generated(request):
    response = render(request, 'QuotePT109/generated.html')
    return response

# Create your views here.
