from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'created_by', 'updated_by')
    search_fields = ('name',)

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'created_at', 'updated_at', 'created_by', 'updated_by')
    search_fields = ('name', 'category__name')

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Subcategory, SubcategoryAdmin)
