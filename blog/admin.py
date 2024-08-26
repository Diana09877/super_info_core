from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from blog.models import Publication, Category, Hashtag

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['id', 'title']


@admin.register(Publication)
class PublicationAdmin(TranslationAdmin):
    list_display = ['id', 'title']

@admin.register(Hashtag)
class HashtagAdmin(TranslationAdmin):
    list_display = ['id', 'title']

# @admin.register(PublicationComment)
# class CreatePublicationCommentAdmin(admin.ModelAdmin):
#     list_display = ['author_name']



