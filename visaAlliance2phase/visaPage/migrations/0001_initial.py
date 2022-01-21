# Generated by Django 3.2 on 2021-05-23 07:10

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubVisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_visa_title', models.TextField(blank=True, max_length=300)),
                ('subvisa_body', ckeditor.fields.RichTextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisaCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visa_image', models.ImageField(blank=True, upload_to='photos/visas')),
                ('visa_title', models.CharField(blank=True, max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('hover_description', models.TextField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='VisaPageDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='VisaDetailsDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_image', models.ImageField(blank=True, upload_to='photos/visas')),
                ('top_image_description', models.TextField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='photos/visas')),
                ('visa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visaPage.visacategory')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfSubVisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('are_you_including_name_of_sub_visa_first_time', models.BooleanField(default=False)),
                ('type_sub_visa_title', models.TextField(blank=True, max_length=250)),
                ('type_of_subvisa_body', ckeditor.fields.RichTextField(blank=True)),
                ('font_awesome_class_name1', models.TextField(blank=True, max_length=100)),
                ('first_field1', models.CharField(blank=True, max_length=100)),
                ('second_field1', models.CharField(blank=True, max_length=200)),
                ('third_field1', ckeditor.fields.RichTextField(blank=True)),
                ('font_awesome_class_name2', models.TextField(blank=True, max_length=100)),
                ('first_field2', models.CharField(blank=True, max_length=100)),
                ('second_field2', models.CharField(blank=True, max_length=200)),
                ('third_field2', ckeditor.fields.RichTextField(blank=True)),
                ('font_awesome_class_name3', models.TextField(blank=True, max_length=100)),
                ('first_field3', models.CharField(blank=True, max_length=100)),
                ('second_field3', models.CharField(blank=True, max_length=200)),
                ('third_field3', ckeditor.fields.RichTextField(blank=True)),
                ('sub_visa_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visaPage.subvisa')),
                ('visa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visaPage.visacategory')),
            ],
        ),
        migrations.AddField(
            model_name='subvisa',
            name='visa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visaPage.visacategory'),
        ),
    ]