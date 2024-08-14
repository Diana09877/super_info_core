from django.contrib import admin
from django.contrib import admin
from blog.models import Publication, Category, Hashtag,PublicationComment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['title']

# @admin.register(PublicationComment)
# class CreatePublicationCommentAdmin(admin.ModelAdmin):
#     list_display = ['author_name']



