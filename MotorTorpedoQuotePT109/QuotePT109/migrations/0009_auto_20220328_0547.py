# Generated by Django 2.1.5 on 2022-03-28 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuotePT109', '0008_philisophicalquote_philisophicalquoteimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finishedquote',
            name='category',
        ),
        migrations.DeleteModel(
            name='FinishedQuote',
        ),
    ]
