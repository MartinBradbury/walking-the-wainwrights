# Generated by Django 4.2.11 on 2024-03-19 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0004_rename_approved_comment_flagged_comment_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='flagged',
            new_name='approved',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='status',
        ),
    ]
