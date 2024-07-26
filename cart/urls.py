# cart/urls.py
from django.urls import path
from .views import CartDetailView, AddToCartView, RemoveFromCartView

urlpatterns = [
    path('store/cart/', CartDetailView.as_view(), name='cart_detail'),
    path('store/cart/add/', AddToCartView.as_view(), name='add_to_cart_ajax'),
    path('store/cart/remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
]
