from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from .models import Product


admin.site.register(Product)
# @admin.register(Product)
# class ProductAdmin(TranslationAdmin):
#         readonly_fields = ("get_image",)
#
#
# def get_image(self, obj):
#      return mark_safe(f'<img src={obj.product.url} width="50" height="60"')
#
# # get_image.short_description = 'Постер'
