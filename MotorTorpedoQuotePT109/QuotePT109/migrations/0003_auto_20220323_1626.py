# Generated by Django 2.1.5 on 2022-03-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuotePT109', '0002_page_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='prompt',
            old_name='prompt',
            new_name='text',
        ),
    ]
