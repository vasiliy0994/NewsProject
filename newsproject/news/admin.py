from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'created_at', 'get_photo', 'published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('published', 'category')
    list_filter = ('published', 'category')
    fields = ('title', 'content', 'category', 'photo', 'get_photo', 'published', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'created_at', 'updated_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" widht="75">')
        else:
            return 'Фото нет'
    get_photo_description = 'миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Страница администратора'
