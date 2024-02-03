from django.urls import path
from .views import ProductDetailsAPIView, TopRatedProductsAPIView, AverageDiscountByCategoryAPIView, ProductsByCategoryAPIView

urlpatterns = [
    path('product/<str:product_id>/', ProductDetailsAPIView.as_view(), name='product-details'),
    path('top-rated/', TopRatedProductsAPIView.as_view(), name='top-rated-products'),
    path('average-discounts/', AverageDiscountByCategoryAPIView.as_view(), name='average-discounts'),
    path('products/<str:category>/', ProductsByCategoryAPIView.as_view(), name='products-by-category'),
]
