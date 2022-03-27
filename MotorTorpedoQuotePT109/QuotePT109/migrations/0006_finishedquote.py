# Generated by Django 2.1.5 on 2022-03-27 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuotePT109', '0005_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinishedQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/FinishedQuotes/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuotePT109.Category')),
            ],
        ),
    ]
