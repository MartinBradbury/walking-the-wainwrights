# Generated by Django 4.2.11 on 2024-03-25 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_gallery_feature_img_alter_gallery_flagged'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='user_img',
        ),
    ]