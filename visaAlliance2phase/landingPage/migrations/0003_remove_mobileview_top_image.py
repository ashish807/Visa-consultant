# Generated by Django 3.2 on 2021-05-25 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0002_auto_20210525_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobileview',
            name='top_image',
        ),
    ]
