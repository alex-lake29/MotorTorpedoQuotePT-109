from django.shortcuts import render
from django.http import HttpResponse
from QuotePT109.models import Category, Page, QuoteImage, Quote
from QuotePT109.forms import UploadForm
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list_likes = Page.objects.order_by('-likes')[:5]
    page_list_views = Page.objects.order_by('views')[:5]
    context_dict={}
    context_dict['liked_pages'] = page_list_likes
    context_dict['viewed_pages'] = page_list_views
    return render(request, 'QuotePT109/index.html', context=context_dict)
    
def generator(request):
    response = render(request, 'QuotePT109/generator.html')
    return response

def generatorC(request):
    form = UploadForm(request.POST, request.FILES)
    response = render(request, 'QuotePT109/generatorC.html', {'form' : form})
    return response

def login(request):
    response = render(request, 'QuotePT109/login.html')
    return response

def preGenerator(request):
    response = render(request, 'QuotePT109/preGenerate.html')
    return response

def generated(request):
    context_dict={}
    context_dict['image'] = QuoteImage.url
    context_dict['quote'] = Quote.quote
    return render(request, 'QuotePT109/generated.html', context=context_dict)
