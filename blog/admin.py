from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Post,Work,Articles,Contacts,News,Aboutcomp
# Register your models here.



@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Contacts)
class ContactsAdmin(TranslationAdmin):
    pass

@admin.register(Post)
class PostAdmin(TranslationAdmin):
    pass

@admin.register(Work)
class WorkAdmin(TranslationAdmin):
    pass

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    pass


@admin.register(Aboutcomp)
class AboutcompAdmin(TranslationAdmin):
    pass