from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Article, GalleryArticle


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name']



class GalleryArticleInline(admin.TabularInline):
    model = GalleryArticle
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'quantity_views', 'is_published',
                    'is_banned', 'create_datetime', 'update_datetime', 'show_photo']
    list_display_links = ['pk', 'title']
    search_fields = ['title']
    list_filter = ['category__name']
    inlines = [GalleryArticleInline]
    prepopulated_fields = {'slug': ['title']}
    list_per_page = 5
    ordering = ['pk']

    @admin.action(description='Фото')
    def show_photo(self, obj):
        try:
            return format_html(f'<img src="{obj.first_photo()}" width=100>')
        except Exception as error:
            print(error)
            return '-'
