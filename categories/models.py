from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='category_created_user', on_delete=models.PROTECT)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='category_updated_user', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subcategory_created_user', on_delete=models.PROTECT)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subcategory_updated_user', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
