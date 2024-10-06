from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Перечисляем поля, отображаемые в таблице списка статей
    list_display = ('name', 'created_at')
    search_fields = ['name', 'body']
    # Перечисляем поля для фильтрации
    list_filter = (('created_at', DateFieldListFilter),)
