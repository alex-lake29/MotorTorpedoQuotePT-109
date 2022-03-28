from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# from populate_QuotePT109 import populate
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
    url = pickImage()

class InspiringQuoteImage(models.Model):
    def pickImage():
        x = random.randint(1,10)
        return("/media/inspiring/"+str(x)+".jpg")
    url = pickImage()

class PhilisophicalQuoteImage(models.Model):
    def pickImage():
        x = random.randint(1,10)
        return("/media/philisophical/"+str(x)+".jpg")
    url = pickImage()

class ComedicQuote(models.Model):
    def generateQuote(type):
        allPrompts = Prompt.objects.filter()
        promptList=[]
        print("hello")
        for i in range (len(allPrompts)):
            x = str(allPrompts[i]).split(":")
            if x[0] == type:
                promptList.append(x[1])
        allNouns = Noun.objects.filter()
        nounList=[]
        for j in range (len(allNouns)):
            y = str(allNouns[j]).split(":")
            if y[0] == type:
                nounList.append(y[1])
        prompt = promptList[random.randint(0,len(promptList)-1)]
        a = nounList[random.randint(0,len(nounList)-1)]
        b = nounList[random.randint(0,len(nounList)-1)]
        c = nounList[random.randint(0,len(nounList)-1)]
        splitPrompt = str(prompt).split("_")
        return (splitPrompt[0]+a+splitPrompt[1]+b+splitPrompt[2]+c)
    quote = generateQuote("c")

class InspiringQuote(models.Model):
    quote = ComedicQuote.generateQuote("i")

class PhilisophicalQuote(models.Model):
    quote = ComedicQuote.generateQuote("i")