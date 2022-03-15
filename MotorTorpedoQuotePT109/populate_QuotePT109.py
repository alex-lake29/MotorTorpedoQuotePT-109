import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MotorTorpedoQuotePT109.settings')

import django
django.setup()
from QuotePT109.models import Category, Page

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
        {'prompt': 'cow'},
        {'prompt': 'egg'},
        {'prompt': 'jimmy carr'}
    ]