# Generated by Django 3.2 on 2021-06-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0005_auto_20210525_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='islidingimage',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='photos/home'),
        ),
    ]
