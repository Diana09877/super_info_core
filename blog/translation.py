from modeltranslation.translator import register, TranslationOptions
from blog.models import Publication, Category, Hashtag

@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'full_description')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Hashtag)
class HashtagTranslationOptions(TranslationOptions):
    fields = ('title',)

# @register(Contact)
# class ContactTranslationOptions(TranslationOptions):
#     fields = ('name', 'email', 'message')

