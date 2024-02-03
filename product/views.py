# In views.py
from collections import defaultdict
import csv
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ProductSerializer





class AverageDiscountByCategoryAPIView(APIView):
    def get(self, request):
        average_discounts = get_average_discounts_by_category()
        return Response(average_discounts)


class ProductsByCategoryAPIView(APIView):
    def get(self, request, category):
        products_in_category = get_products_by_category(category)
        serializer = ProductSerializer(products_in_category, many=True)
        return Response(serializer.data)


def get_average_discounts_by_category():
    category_discounts = defaultdict(list)

    with open('C:/Users/fazi/Desktop/foxiom/dataset.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            categories = row['category'].split('|')
            for category in categories:
                category_discounts[category].append(float(row['discount_percentage'].rstrip('%')))

    # Calculate average discount for each category
    average_discounts = {category: "{:.2f}%".format(sum(discounts) / len(discounts)) for category, discounts in category_discounts.items()}
    return average_discounts


def get_products_by_category(category):
    products_in_category = []

    with open('C:/Users/fazi/Desktop/foxiom/dataset.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            categories = row['category'].split('|')
            if any(category.lower() in cat.lower() for cat in categories):
                product_details = {
                    'product_id': row['product_id'],
                    'product_name': row['product_name'],
                    # 'about_product' : row['about_product'],
                    # 'user_id' : row['user_id'],
                    # 'user_name' : row['user_name'],
                    'rating': float(row['rating']),
                    # 'discounted_price': row['discounted_price'],
                    'actual_price': row['actual_price'],
                    # 'discount_percentage': row['discount_percentage'],
                    'category': categories,
                }
                products_in_category.append(product_details)

    return products_in_category
