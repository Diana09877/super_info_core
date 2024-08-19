
from django.db.models import Count
from django.db.models.functions import datetime
from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.TextField()

    class Meta:
        verbose_name_plural = 'Категории публикаций'
        verbose_name = 'Категория публикации'

    def __str__(self):
        return self.title

class Hashtag(models.Model):
    title = models.TextField()

    class Meta:
        verbose_name_plural = 'Хештеги'
        verbose_name = 'Хештег'

    def __str__(self):
        return self.title



class Publication(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="publications", null=True)
    hashtags = models.ManyToManyField(Hashtag, related_name='publications')
    title = models.TextField(verbose_name='название')
    short_description = models.TextField(verbose_name='короткое описание')
    full_description = models.TextField(verbose_name='полное описание', default=None)
    image = models.ImageField(verbose_name='изображение',null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
   # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'



class PublicationComment(models.Model):
    publication = models.ForeignKey(Publication,related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(verbose_name='имя автора',max_length=200, default=None)
    comment_text = models.TextField(verbose_name='текст комментария', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author_name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
