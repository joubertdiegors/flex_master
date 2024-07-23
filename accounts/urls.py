from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterBasicView.as_view(), name='register'),
    path('complete_registration/<int:customer_id>/', views.CompleteRegistrationView.as_view(), name='complete_registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]