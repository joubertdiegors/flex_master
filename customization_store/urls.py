from django.urls import path
from . import views

urlpatterns = [
    path('customization/', views.CustomizationHomeView.as_view(), name='customization_home'),

    path('customization/header/', views.UploadHeaderLogoView.as_view(), name='upload_header_logo'),
    path('customization/navbar/', views.UploadNavbarLogoView.as_view(), name='upload_navbar_logo'),
    path('customization/favicon/', views.UploadFaviconView.as_view(), name='upload_favicon'),
    path('customization/product_default/', views.UploadProductImageDefaultView.as_view(), name='upload_product_image_default'),
    path('customization/customer_default/', views.UploadCustomerImageDefaultView.as_view(), name='upload_customer_image_default'),
    path('customization/supplier_default/', views.UploadSupplierImageDefaultView.as_view(), name='upload_supplier_image_default'),
    path('shipping_information/home/edit/', views.edit_content, name='edit_content'),

    path('customization/banner/list/', views.BannerListView.as_view(), name='banner_list'),
    path('customization/banner/create/', views.BannerCreateView.as_view(), name='banner_create'),
    path('customization/banner/<int:pk>/edit/', views.BannerUpdateView.as_view(), name='banner_update'),
    path('customization/banner/delete/<int:pk>/', views.BannerDeleteView.as_view(), name='banner_delete'),

    path('customization/best_sellers/', views.BestSellerProductListView.as_view(), name='best_seller_list'),
    path('customization/best_sellers/new/', views.BestSellerProductCreateView.as_view(), name='best_seller_create'),
    path('customization/best_sellers/<int:pk>/edit/', views.BestSellerProductUpdateView.as_view(), name='best_seller_update'),
    path('customization/best_sellers/<int:pk>/delete/', views.BestSellerProductDeleteView.as_view(), name='best_seller_delete'),

    path('customization/fresh_products/', views.FreshProductsListView.as_view(), name='fresh_product_list'),
    path('customization/fresh_products/new/', views.FreshProductsCreateView.as_view(), name='fresh_product_create'),
    path('customization/fresh_products/<int:pk>/edit/', views.FreshProductsUpdateView.as_view(), name='fresh_product_update'),
    path('customization/fresh_products/<int:pk>/delete/', views.FreshProductsDeleteView.as_view(), name='fresh_product_delete'),

    path('highlighted_brands/', views.HighlightedBrandListView.as_view(), name='highlighted_brand_list'),
    path('highlighted_brands/new/', views.HighlightedBrandCreateView.as_view(), name='highlighted_brand_create'),
    path('highlighted_brands/<int:pk>/edit/', views.HighlightedBrandUpdateView.as_view(), name='highlighted_brand_update'),
    path('highlighted_brands/<int:pk>/delete/', views.HighlightedBrandDeleteView.as_view(), name='highlighted_brand_delete'),
]
