from django.contrib import admin
from QuotePT109.models import Category, Page, Prompt, Noun
# Register your models here.
admin.site.register(Page)
admin.site.register(Category)
admin.site.register(Prompt)
admin.site.register(Noun)