from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cate_parent_id', 'cate_name', 'cate_id']
    ordering = ['cate_parent_id']
    search_fields = ['cate_name']

class NewsBannerAdmin(admin.ModelAdmin):
    list_display = ['new_name', 'new_date']
    ordering = ['new_date']
    list_filter = ['new_date']

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_detail_name', 'cate_id', 'product_detail_price']
    ordering = ['product_detail_date']
    list_filter = ['product_detail_date']
    inlines = [ProductImageInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id', 'product_color', 'product_size', 'product_quantity', 'product_date']
    ordering = ['product_date']
    list_filter = ['product_date']

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_id', 'tag_name']

class TagMapAdmin(admin.ModelAdmin):
    list_display = ['tag_map_id', 'product_id', 'tag_id']

class ColorAdmin(admin.ModelAdmin):
    list_display = ['color_id', 'color_name']

class SizeAdmin(admin.ModelAdmin):
    list_display = ['size_id', 'size_name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(NewsBanner, NewsBannerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(TagMap, TagMapAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)