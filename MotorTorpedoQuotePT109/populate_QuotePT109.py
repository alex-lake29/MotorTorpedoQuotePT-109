import os

from sympy import I
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MotorTorpedoQuotePT109.settings')

import django
django.setup()
from QuotePT109.models import Prompt, Page, Category, Noun

def populate():
    prompts = [
        'c:What do you call a _/without a _?/a _',
        'c:How many _/does it take to fix a _? /_',
        'c:What did the _/say to the _?/You are a _',
        'c:Did you hear about the _ /who ran into the _? /He _',
        'c:What does a _/and a _ have in common?/They both eat _s',
        'i:_ is/_ with extra/_',
        'i:_ can be achieved/only with _/and _',
        'i:_ is not about/_, Its about/_',
        'i:_ cannot exist without _/which cannot exist/without _',
        'i:with _/_ and _/You can do anything!',
        'p:To engage in_/is equal to _/to those who are _',
        'p:To engage in _/or to engage in _?/Are they both not _?'
    ]

    nouns = ['c:chicken','c:cow','c:egg','c:jimmy carr','c:rango enjoyer','c:django programmer','c:maths student',
        'c:auroch','c:englishman','c:manchester united fan','c:officer of the law','c:james may', 'i:Hard Work',
        'i:Dedication','i:Perseverance','i:The Grindset','i:Success','i:Excellence','i:Inspiration',
        'p:Pondering','p:Questioning','p:Believing','p:Thinking','p:Wandering ones lands','p:seek salvation','p:Pondering the orb',
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

    for i in prompts:
        cp = add_prompt(i)
    for i in nouns:
        cp = add_noun(i)

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

def add_prompt(prompt):
    cp = Prompt.objects.get_or_create(text=prompt)[0]
    cp.save()
    return cp

def add_noun(noun):
    cn = Noun.objects.get_or_create(text=noun)[0]
    cn.save()
    return cn

if __name__ == '__main__':
    print('Starting QuotePT109 population script...')
    populate()