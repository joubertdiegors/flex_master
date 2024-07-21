from django.urls import path
from . import views

urlpatterns = [
    path('country/list', views.CountryListView.as_view(), name='country_list'),
    path('country/create', views.CountryCreateView.as_view(), name='country_create'),
    path('country/<int:pk>/detail', views.CountryDetailView.as_view(), name='country_detail'),
    path('country/<int:pk>/update', views.CountryUpdateView.as_view(), name='country_update'),
]