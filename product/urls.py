from django.urls import path
from .views import *

urlpatterns = [

    path('average-discounts/', AverageDiscountByCategoryAPIView.as_view(), name='average-discounts'),
    path('products/<str:category>/', ProductsByCategoryAPIView.as_view(), name='products-by-category'),
]
