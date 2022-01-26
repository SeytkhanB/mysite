
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published',
              'numbers_of_views', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'numbers_of_views', 'created_at', 'updated_at')
    save_on_top = True 

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="91">')
        else:
            return "-"

    get_photo.short_description = 'Photo'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'News management'
admin.site.site_header = 'News management'


