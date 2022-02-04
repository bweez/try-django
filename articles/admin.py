from django.contrib import admin

# Register your models here.
# This builds the admin page for articles
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['id', 'title', 'timestamp', 'updated']


admin.site.register(Article, ArticleAdmin)
