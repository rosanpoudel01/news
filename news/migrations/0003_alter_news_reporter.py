# Generated by Django 4.1.5 on 2023-01-31 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_category_options_alter_news_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='reporter',
            field=models.CharField(max_length=255),
        ),
    ]
