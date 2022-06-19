from modeltranslation.translator import register, TranslationOptions
from .models import Contacts,Post,Work,News,Aboutcomp



@register(Contacts)
class ContactsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

@register(Work)
class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'totle',)

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

@register(Aboutcomp)
class AboutcompTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)