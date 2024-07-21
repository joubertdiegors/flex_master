from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    path('products/ingredients/<int:pk>/', views.IngredientsCreateView.as_view(), name='ingredients_create'),

    path('products/nutritionalitems/', views.NutritionalItemListView.as_view(), name='nutritional_item_list'),
    path('products/nutritionalitems/new/', views.NutritionalItemCreateView.as_view(), name='nutritional_item_create'),
    path('products/nutritionalitems/<int:pk>/edit/', views.NutritionalItemUpdateView.as_view(), name='nutritional_item_update'),
    path('products/nutritionalitems/<int:pk>/delete/', views.NutritionalItemDeleteView.as_view(), name='nutritional_item_delete'),

    path('products/nutritionalinfo/<int:pk>', views.NutritionalInfoView.as_view(), name='nutritional_info_create'),
    path('products/nutritionalinfo/delete/<int:pk>/', views.NutritionalInfoDeleteView.as_view(), name='nutritional_info_delete'),

    path('brands/', views.BrandListView.as_view(), name='brand_list'),
    path('brands/create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('brands/<int:pk>/', views.BrandDetailView.as_view(), name='brand_detail'),
    path('brands/<int:pk>/update/', views.BrandUpdateView.as_view(), name='brand_update'),
    path('brands/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand_delete'),

    path('sales_unit/', views.SalesUnitListView.as_view(), name='sales_unit_list'),
    path('sales_unit/create/', views.SalesUnitCreateView.as_view(), name='sales_unit_create'),
    path('sales_unit/<int:pk>/', views.SalesUnitDetailView.as_view(), name='sales_unit_detail'),
    path('sales_unit/<int:pk>/update/', views.SalesUnitUpdateView.as_view(), name='sales_unit_update'),
    path('sales_unit/<int:pk>/delete/', views.SalesUnitDeleteView.as_view(), name='sales_unit_delete'),

    path('package_unit/', views.PackageUnitListView.as_view(), name='package_unit_list'),
    path('package_unit/create/', views.PackageUnitCreateView.as_view(), name='package_unit_create'),
    path('package_unit/<int:pk>/', views.PackageUnitDetailView.as_view(), name='package_unit_detail'),
    path('package_unit/<int:pk>/update/', views.PackageUnitUpdateView.as_view(), name='package_unit_update'),
    path('package_unit/<int:pk>/delete/', views.PackageUnitDeleteView.as_view(), name='package_unit_delete'),
]
