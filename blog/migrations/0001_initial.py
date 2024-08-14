# Generated by Django 5.0.8 on 2024-08-13 19:12

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Категория публикации',
                'verbose_name_plural': 'Категории публикаций',
            },
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Хештег',
                'verbose_name_plural': 'Хештеги',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(verbose_name='название')),
                ('short_description', ckeditor.fields.RichTextField(verbose_name='короткое описание')),
                ('full_description', ckeditor.fields.RichTextField(default=None, verbose_name='полное описание')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publications', to='blog.category')),
                ('hashtags', models.ManyToManyField(related_name='publications', to='blog.hashtag')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
        migrations.CreateModel(
            name='PublicationComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', ckeditor.fields.RichTextField(default=None, max_length=200, verbose_name='имя автора')),
                ('comment_text', models.TextField(null=True, verbose_name='текст комментария')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.publication')),
            ],
        ),
    ]
