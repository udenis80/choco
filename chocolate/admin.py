from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product

admin.site.register(Category)

@admin.register(Product)
class Product(admin.ModelAdmin):
    """Продукты"""
    list_display = ('name', 'price', 'get_image')
    readonly_fields = ('get_image')
    def get_image(self,obj):
        return mark_safe(f'<img scr={obj.image.url} width="50", height="40"')
    # get_image.short_description='Изображение'