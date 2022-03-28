from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# from populate_QuotePT109 import populate
import random

# Create your models here.
# class Prompt(models.Model):
#     text = models.CharField(max_length=128, unique=True)
#     def __str__(self):
#         return self.text

class Noun(models.Model):
    text = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.text

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class ComedicQuoteImage(models.Model):
    def pickImage():
        x = random.randint(1,10)
        return("/media/comedic/"+str(x)+".jpg")
    url = pickImage

class InspiringQuoteImage(models.Model):
    def pickImage():
        x = random.randint(1,10)
        return("/media/inspiring/"+str(x)+".jpg")
    url = pickImage

class PhilisophicalQuoteImage(models.Model):
    def pickImage():
        x = random.randint(1,10)
        return("/media/philisophical/"+str(x)+".jpg")
    url = pickImage

class ComedicPrompt(models.Model):
    text = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.text

class InspiringPrompt(models.Model):
    text = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.text

class PhilisophicalPrompt(models.Model):
    text = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.text

class ComedicNoun(models.Model):
    text = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.text

class InspiringNoun(models.Model):
    text = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.text
    
class PhilisophicalNoun(models.Model):
    text = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.text

class ComedicQuote(models.Model):
    def generateQuote():
        prompt = ComedicPrompt.objects.filter()[random.randint(0,len(ComedicPrompt.objects.filter())-1)]
        x = str(ComedicNoun.objects.filter()[random.randint(0,len(ComedicNoun.objects.filter())-1)])
        y = str(ComedicNoun.objects.filter()[random.randint(0,len(ComedicNoun.objects.filter())-1)])
        z = str(ComedicNoun.objects.filter()[random.randint(0,len(ComedicNoun.objects.filter())-1)])
        splitPrompt = str(prompt).split("_")
        return (splitPrompt[0]+x+splitPrompt[1]+y+splitPrompt[2]+z)
    quote = generateQuote

class InspiringQuote(models.Model):
    def generateQuote():
        prompt = InspiringPrompt.objects.filter()[random.randint(0,len(InspiringPrompt.objects.filter())-1)]
        print(prompt)
        x = str(InspiringNoun.objects.filter()[random.randint(0,len(InspiringNoun.objects.filter())-1)])
        y = str(InspiringNoun.objects.filter()[random.randint(0,len(InspiringNoun.objects.filter())-1)])
        z = str(InspiringNoun.objects.filter()[random.randint(0,len(InspiringNoun.objects.filter())-1)])
        splitPrompt = str(prompt).split("_")
        return (splitPrompt[0]+x+splitPrompt[1]+y+splitPrompt[2]+z)
    quote = generateQuote

class PhilisophicalQuote(models.Model):
    def generateQuote():
        prompt = PhilisophicalPrompt.objects.filter()[random.randint(0,len(PhilisophicalPrompt.objects.filter())-1)]
        x = str(PhilisophicalNoun.objects.filter()[random.randint(0,len(PhilisophicalNoun.objects.filter())-1)])
        y = str(PhilisophicalNoun.objects.filter()[random.randint(0,len(PhilisophicalNoun.objects.filter())-1)])
        z = str(PhilisophicalNoun.objects.filter()[random.randint(0,len(PhilisophicalNoun.objects.filter())-1)])
        splitPrompt = str(prompt).split("_")
        return (splitPrompt[0]+x+splitPrompt[1]+y+splitPrompt[2]+z)
    quote = generateQuote