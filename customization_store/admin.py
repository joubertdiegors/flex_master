from django.contrib import admin
from .models import Banner, BestSellerProduct, FreshProducts, HighlightedBrand

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link', 'start_date', 'end_date', 'active')
    search_fields = ('title', 'description')

admin.site.register(Banner, BannerAdmin)

class BestSellerProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at', 'created_by')
    search_fields = ('product__name', 'description')
    readonly_fields = ('created_at', 'created_by')

admin.site.register(BestSellerProduct, BestSellerProductAdmin)

class FreshProductsAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at', 'created_by')
    search_fields = ('product__name', 'description')
    readonly_fields = ('created_at', 'created_by')

admin.site.register(FreshProducts, FreshProductsAdmin)

class HighlightedBrandAdmin(admin.ModelAdmin):
    list_display = ('brand', 'created_at', 'created_by')
    search_fields = ('brand__name', 'description')
    readonly_fields = ('created_at', 'created_by')

admin.site.register(HighlightedBrand, HighlightedBrandAdmin)
