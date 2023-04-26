from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path('shop', views.shop, name='shop'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]