from django.shortcuts import render
from django.http import HttpResponse
from QuotePT109.models import Category, Page, ComedicQuoteImage, ComedicQuote, InspiringQuoteImage, InspiringQuote, PhilisophicalQuote, PhilisophicalQuoteImage
# from QuotePT109.forms import UploadForm
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list_likes = Page.objects.order_by('-likes')[:5]
    page_list_views = Page.objects.order_by('views')[:5]
    context_dict={}
    context_dict['liked_pages'] = page_list_likes
    context_dict['viewed_pages'] = page_list_views
    context_dict['class'] = "home"
    return render(request, 'QuotePT109/index.html', context=context_dict)
    
def generator(request):
    response = render(request, 'QuotePT109/generator.html')
    return response

def login(request):
    response = render(request, 'QuotePT109/login.html')
    return response

def preGenerator(request):
    context_dict={}
    context_dict['class'] = "select"
    response = render(request, 'QuotePT109/preGenerate.html', context=context_dict)
    return response

def comedicGenerated(request):
    context_dict={}
    context_dict['image'] = ComedicQuoteImage.url
    context_dict['quote'] = ComedicQuote.quote
    context_dict['class'] = "comedic"
    context_dict['title'] = "Comedic Joke"
    return render(request, 'QuotePT109/Generated.html', context=context_dict)

def inspirationalGenerated(request):
    context_dict={}
    context_dict['image'] = InspiringQuoteImage.url
    context_dict['quote'] = InspiringQuote.quote
    context_dict['class'] = "inspiring"
    context_dict['title'] = "Beautiful Quote"
    return render(request, 'QuotePT109/Generated.html', context=context_dict)

def philisophicalGenerated(request):
    context_dict={}
    context_dict['image'] = PhilisophicalQuoteImage.url
    context_dict['quote'] = PhilisophicalQuote.quote
    context_dict['class'] = "philisophical"
    context_dict['title'] = "Philisophical Quote"
    return render(request, 'QuotePT109/Generated.html', context=context_dict)
