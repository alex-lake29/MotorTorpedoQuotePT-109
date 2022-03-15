from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Prompt(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name