from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    # path("<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]