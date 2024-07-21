# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('administration/categories/list/', views.CategoryListView.as_view(), name='category_list'),
    path('administration/categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('administration/categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('administration/categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('administration/subcategories/list/<int:category_id>/', views.SubcategoryListView.as_view(), name='subcategory_list'),
    path('administration/subcategories/create/', views.SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('administration/subcategories/<int:pk>/update/', views.SubcategoryUpdateView.as_view(), name='subcategory_update'),
    path('administration/subcategories/delete/<int:pk>/', views.SubcategoryDeleteView.as_view(), name='subcategory_delete'),
    
    path('administration/subcategories/<int:category_id>/', views.subcategories_by_category, name='subcategories_by_category'),
]
