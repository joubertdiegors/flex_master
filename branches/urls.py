from django.urls import path
from . import views

urlpatterns = [
    path('branches/list', views.BranchListView.as_view(), name='branch_list'),
    path('branches/create', views.BranchCreateView.as_view(), name='branch_create'),
    path('branches/<int:pk>/detail', views.BranchDetailView.as_view(), name='branch_detail'),
    path('branches/<int:pk>/update', views.BranchUpdateView.as_view(), name='branch_update'),
]