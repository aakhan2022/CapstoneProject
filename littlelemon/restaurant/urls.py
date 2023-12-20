from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('menu-items/', views.MenuItemView.as_view(), name='all-menu-items'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
]