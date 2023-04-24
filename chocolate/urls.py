from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path('products/<int:product_id>/', views.product_view, name='product_detail'),
    # path("<slug:slug>/", views.product_detail(), name="movie_detail"),

]