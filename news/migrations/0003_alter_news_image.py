# Generated by Django 4.2.4 on 2024-02-19 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Фотография'),
        ),
    ]