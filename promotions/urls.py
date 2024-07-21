from django.urls import path
from . import views

urlpatterns = [
    path('promotions/', views.PromotionListView.as_view(), name='promotion_list'),
    path('promotions/create/', views.PromotionCreateView.as_view(), name='promotion_create'),
    path('promotions/<int:pk>/', views.PromotionDetailView.as_view(), name='promotion_detail'),
    path('promotions/<int:pk>/update/', views.PromotionUpdateView.as_view(), name='promotion_update'),
    path('promotions/<int:pk>/delete/', views.PromotionDeleteView.as_view(), name='promotion_delete'),
]