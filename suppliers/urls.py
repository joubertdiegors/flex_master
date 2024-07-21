from django.urls import path
from . import views

urlpatterns = [
    path('supplier_type/', views.SupplierTypeListView.as_view(), name='supplier_type_list'),
    path('supplier_type/create/', views.SupplierTypeCreateView.as_view(), name='supplier_type_create'),
    path('supplier_type/<int:pk>/detail/', views.SupplierTypeDetailView.as_view(), name='supplier_type_detail'),
    path('supplier_type/<int:pk>/update/', views.SupplierTypeUpdateView.as_view(), name='supplier_type_update'),

    path('supplier_state/', views.SupplierStateListView.as_view(), name='supplier_state_list'),
    path('supplier_state/create/', views.SupplierStateCreateView.as_view(), name='supplier_state_create'),
    path('supplier_state/<int:pk>/detail/', views.SupplierStateDetailView.as_view(), name='supplier_state_detail'),
    path('supplier_state/<int:pk>/update/', views.SupplierStateUpdateView.as_view(), name='supplier_state_update'),

    path('supplier/', views.SupplierListView.as_view(), name='supplier_list'),
    path('supplier/create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier/<int:pk>/detail/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/<int:pk>/update/', views.SupplierUpdateView.as_view(), name='supplier_update'),
]
