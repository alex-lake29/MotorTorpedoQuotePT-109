from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import random

# Create your models here.
class Prompt(models.Model):
    text = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.text

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

class QuoteImage(models.Model):
    def pickImage():
        x = random.randint(1,10)
        return("/media/comedic/"+str(x)+".jpg")
    url = pickImage()

class Quote(models.Model):
    def generateQuote():
        prompt = Prompt.objects.filter()[random.randint(0,4)]
        x = str(Noun.objects.filter()[random.randint(0,11)])
        y = str(Noun.objects.filter()[random.randint(0,11)])
        z = str(Noun.objects.filter()[random.randint(0,11)])
        splitPrompt = str(prompt).split("_")
        return (splitPrompt[0]+x+splitPrompt[1]+y+splitPrompt[2]+z)
    quote = generateQuote
