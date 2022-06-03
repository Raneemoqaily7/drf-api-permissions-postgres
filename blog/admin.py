from django.contrib import admin
from .models import Article



class AdminArticle (admin.ModelAdmin):
    list_display = ["title","author","time_created","time_updated","content"]

admin.site.register(Article,AdminArticle)
