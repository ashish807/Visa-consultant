# Generated by Django 3.2 on 2021-05-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavFooterContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_nav_image', models.ImageField(upload_to='photos/navFooter')),
                ('top_left_button_name', models.CharField(blank=True, max_length=100)),
                ('top_left_button_hyperlink', models.TextField(blank=True, max_length=500)),
                ('top_right_button_name', models.CharField(blank=True, max_length=100)),
                ('top_right_button_hyperlink', models.TextField(blank=True, max_length=500)),
                ('footer_consultation_title', models.TextField(blank=True, max_length=500)),
                ('footer_consultation_title_description', models.TextField(blank=True, max_length=500)),
                ('footer_consultation_button_name', models.TextField(blank=True, max_length=500)),
                ('footer_consultation_image', models.ImageField(upload_to='photos/navFooter')),
                ('footer_accreditations_memberships_title', models.TextField(blank=True, max_length=500)),
                ('footer_legal_title', models.TextField(blank=True, max_length=500)),
                ('footer_australia_flag', models.ImageField(upload_to='photos/navFooter')),
                ('footer_australia_headoffice_title', models.TextField(blank=True, max_length=300)),
                ('footer_australia_address', models.TextField(blank=True, max_length=300)),
                ('footer_australia_facebook_link', models.TextField(blank=True, max_length=500)),
                ('footer_australia_instagram_link', models.TextField(blank=True, max_length=500)),
                ('footer_nepali_flag', models.ImageField(upload_to='photos/navFooter')),
                ('footer_nepal_headoffice_title', models.TextField(blank=True, max_length=300)),
                ('footer_nepali_address', models.TextField(blank=True, max_length=300)),
                ('footer_nepali_facebook_link', models.TextField(blank=True, max_length=500)),
                ('footer_nepali_instagram_link', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
