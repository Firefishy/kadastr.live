# Generated by Django 3.1.4 on 2022-01-18 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadinfo', '0007_update_latest_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='latest_level',
        ),
    ]
