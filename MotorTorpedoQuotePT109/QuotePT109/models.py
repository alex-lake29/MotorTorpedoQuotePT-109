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

class ComedicQuoteImage(models.Model):
    def pickImage():
        x = random.randint(1,10)
        return("/media/comedic/"+str(x)+".jpg")
    url = pickImage

def generateQuote(type):
        allPrompts = Prompt.objects.filter()
        prompts=[]
        for i in range (len(allPrompts)):
            x = str(allPrompts[i]).split(":")
            if x[0] == type:
                prompts.append(x[1])
        allNouns = Noun.objects.filter()
        nouns=[]
        for j in range (len(allNouns)):
            y = str(allNouns[j]).split(":")
            print(y[0])
            if y[0] == type:
                nouns.append(y[1])
        print(len(nouns)-1)
        prompt = prompts[random.randint(0,len(prompts)-1)]
        a = nouns[random.randint(0,len(nouns)-1)]
        b = nouns[random.randint(0,len(nouns)-1)]
        c = nouns[random.randint(0,len(nouns)-1)]
        splitPrompt = str(prompt).split("_")
        return (splitPrompt[0]+a+splitPrompt[1]+b+splitPrompt[2]+c)

class ComedicQuote(models.Model):
    quote = generateQuote("c")

# class Quote(models.Model):
#     quote = generateQuote("i")

class FinishedQuote(models.Model):
    image = models.ImageField(upload_to='static/FinishedQuotes/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)