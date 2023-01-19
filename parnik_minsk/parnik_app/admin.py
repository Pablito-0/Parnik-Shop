from django.contrib import admin
from django.utils.safestring import mark_safe

from parnik_app.models import Product, Category


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'cost', 'article', 'time_create', 'available', 'photo')
    search_fields = ('title', 'cost')
    list_filter = ('category', 'cost')
    list_editable = ('cost', 'available')
    prepopulated_fields = {'slug': ('title',)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Предпросмотр'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, GoodsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_title = 'Админка онлайн-магазина "Парник"'
admin.site.site_header = 'Админ-панель онлайн-магазина "Парник"'
