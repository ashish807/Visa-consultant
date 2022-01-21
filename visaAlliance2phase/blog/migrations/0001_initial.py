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
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_top_image', models.ImageField(upload_to='photos/blog')),
                ('blog_top_description', models.TextField(default='BLOG SINGLE', max_length=100)),
                ('image', models.ImageField(upload_to='photos/blog')),
                ('title', models.TextField(max_length=100, unique=True)),
                ('slug', models.TextField(max_length=100, unique=True)),
                ('short_description', models.TextField(max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('youtube_video_link', models.TextField(blank=True, max_length=100)),
                ('quote_image', models.ImageField(blank=True, upload_to='photos/blog')),
                ('quote_of_the_day', models.TextField(blank=True, max_length=200)),
                ('author', models.CharField(blank=True, max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]