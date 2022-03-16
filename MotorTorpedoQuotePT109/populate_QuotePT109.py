import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MotorTorpedoQuotePT109.settings')

import django
django.setup()
from QuotePT109.models import Prompt, Page, Category

def populate():
    comedic_prompts = [
        {'prompt': 'What do you call a _ without a _? a _'},
        {'prompt': 'How many _ does it take to fix a _? _'},
        {'prompt': 'What does the _ say to the _? You are a _'},
        {'prompt': 'Did you hear about the _ who ran into the _? He _'}
    ]
    inspiring_prompts = [
        {'prompt': 'There is no such thing as _ without _'},
        {'prompt': '_ can be achieved only with _'},
        {'prompt': 'One cannot _ without a good amount of _'},
        {'prompt': '_ is the spice of life, and so is _'}
    ]
    philisophical_prompts = [
        {'prompt': 'What do you call a _ without a _? a _'},
        {'prompt': 'How many _ does it take to fix a _? _'},
        {'prompt': 'What does the _ say to the _? You are a _'},
        {'prompt': 'Did you hear about the _ who ran into the _? He _'}
    ]
    comedic_noun = [
        {'noun': 'chicken'},
        {'noun': 'cow'},
        {'noun': 'egg'},
        {'noun': 'jimmy carr'}
    ]

    inspiring_pages = [
        {'title': 'Official Python Tutorial','url':'http://docs.python.org/3/tutorial/','views': 31},
        {'title':'How to Think like a Computer Scientist','url':'http://www.greenteapress.com/thinkpython/','views': 47},
        {'title':'Learn Python in 10 Minutes','url':'http://www.korokithakis.net/tutorials/python/','views': 98} ]

    philisophical_pages = [
        {'title':'Official Django Tutorial','url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/','views': 120},
        {'title':'Django Rocks','url':'http://www.djangorocks.com/','views': 135},
        {'title':'How to Tango with Django','url':'http://www.tangowithdjango.com/','views': 78} ]
    
    comedic_pages = [
        {'title':'Bottle','url':'http://bottlepy.org/docs/dev/','views': 16},
        {'title':'Flask','url':'http://flask.pocoo.org','views': 45} ]

    cats = {'Inspiring': {'pages': inspiring_pages, 'likes': 64, 'views': 128},
            'Philisophical': {'pages': philisophical_pages, 'likes': 32, 'views': 64},
            'Comedic': {'pages': comedic_pages,'likes': 16, 'views': 32}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])
        
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

    for prompt in comedic_prompts.items():
         c = add_comedic_prompt(prompt)

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_comedic_prompt(prompt):
    c = Category.objects.get_or_create(prompt=prompt)[0]
    c.save()
    return c

if __name__ == '__main__':
    print('Starting QuotePT109 population script...')
    populate()