import os

from sympy import I
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MotorTorpedoQuotePT109.settings')

import django
django.setup()
from QuotePT109.models import Prompt, Page, Category, Noun

def populate():
    comedic_prompts = [
        'What do you call a _ /without a _? /a _',
        'How many _ /does it take to fix a _? /_',
        'What did the _ /say to the _? /You are a _',
        'Did you hear about the _ /who ran into the _? /He _',
        'What does a _ /and a _ have in common? /They both eat _s'
    ]
    inspiring_prompts = [
        {'text': 'There is no such thing as _ without _'},
        {'text': '_ can be achieved only with _'},
        {'text': 'One cannot _ without a good amount of _'},
        {'text': '_ is the spice of life, and so is _'}
    ]
    philisophical_prompts = [
        {'prompt': 'What do you call a _ without a _? a _'},
        {'prompt': 'How many _ does it take to fix a _? _'},
        {'prompt': 'What does the _ say to the _? You are a _'},
        {'prompt': 'Did you hear about the _ who ran into the _? He _'}
    ]
    comedic_nouns = ['chicken','cow','egg','jimmy carr','rango enjoyer','django programmer','maths student',
        'auroch','englishman','manchester united fan','officer of the law','the good the bad and the ugly fan'
    ]

    inspiring_pages = [
        {'title': 'Official Python Tutorial','url':'http://docs.python.org/3/tutorial/','views': 31,'likes':24},
        {'title':'How to Think like a Computer Scientist','url':'http://www.greenteapress.com/thinkpython/','views': 47,'likes':52},
        {'title':'Learn Python in 10 Minutes','url':'http://www.korokithakis.net/tutorials/python/','views': 98,'likes':12} ]

    philisophical_pages = [
        {'title':'Official Django Tutorial','url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/','views': 120,'likes':13},
        {'title':'Django Rocks','url':'http://www.djangorocks.com/','views': 135,'likes':52},
        {'title':'How to Tango with Django','url':'http://www.tangowithdjango.com/','views': 78,'likes':33} ]
    
    comedic_pages = [
        {'title':'Bottle','url':'http://bottlepy.org/docs/dev/','views': 16,'likes':11},
        {'title':'Flask','url':'http://flask.pocoo.org','views': 45,'likes':73} ]

    cats = {'Inspiring': {'pages': inspiring_pages, 'likes': 64, 'views': 128},
            'Philisophical': {'pages': philisophical_pages, 'likes': 32, 'views': 64},
            'Comedic': {'pages': comedic_pages,'likes': 16, 'views': 32}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'], p['likes'])

    for i in comedic_prompts:
        cp = add_comedic_prompt(i)
    for i in comedic_nouns:
        cp = add_comedic_noun(i)

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c

def add_page(cat, title, url, views, likes):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.likes=likes
    p.save()
    return p

def add_comedic_prompt(prompt):
    cp = Prompt.objects.get_or_create(text=prompt)[0]
    cp.save()
    return cp

def add_comedic_noun(noun):
    cn = Noun.objects.get_or_create(text=noun)[0]
    cn.save()
    return cn

if __name__ == '__main__':
    print('Starting QuotePT109 population script...')
    populate()