# Generated by Django 4.2.11 on 2024-03-25 18:31

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_wainwright_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('img_1', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('img_2', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('img_3', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
        ),
    ]