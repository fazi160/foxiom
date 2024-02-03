# In views.py
from collections import defaultdict
import csv
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ProductSerializer


class ProductDetailsAPIView(APIView):
    def get(self, request, product_id):
        product_data = get_product_by_id(product_id)
        if product_data:
            serializer = ProductSerializer(product_data)
            return Response(serializer.data)
        else:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)


class TopRatedProductsAPIView(APIView):
    def get(self, request):
        top_rated_products = get_top_rated_products()
        serializer = ProductSerializer(top_rated_products, many=True)
        return Response(serializer.data)


class AverageDiscountByCategoryAPIView(APIView):
    def get(self, request):
        average_discounts = get_average_discounts_by_category()
        return Response(average_discounts)


class ProductsByCategoryAPIView(APIView):
    def get(self, request, category):
        try:
            products_in_category = get_products_by_category(category)
            if not products_in_category:
                return Response({'error': f'No products found for category: {category}'}, status=status.HTTP_404_NOT_FOUND)

            serializer = ProductSerializer(products_in_category, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def get_product_by_id(product_id):
    with open('dataset.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['product_id'] == product_id:
                return {
                    'product_id': row['product_id'],
                    'product_name': row['product_name'],
                    'category': row['category'].split('|'),
                    'discounted_price': row['discounted_price'],
                    'actual_price': row['actual_price'],
                    'discount_percentage': row['discount_percentage'],
                    'rating': float(row['rating']),
                    'about_product': row['about_product'],
                    'img_link': row['img_link'],
                    'product_link': row['product_link']
                }
    return None


def get_top_rated_products():
    all_products = []

    with open('dataset.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                rating = float(row['rating'])
            except ValueError:
          
                continue

            product_details = {
                'product_id': row['product_id'],
                'product_name': row['product_name'],
                'category': row['category'].split('|'),
                'discounted_price': row['discounted_price'],
                'actual_price': row['actual_price'],
                'discount_percentage': row['discount_percentage'],
                'rating': rating,
                'about_product': row['about_product'],
                'img_link': row['img_link'],
                'product_link': row['product_link']
            }
            all_products.append(product_details)

    # Sort all products by rating in descending order
    sorted_products = sorted(all_products, key=lambda x: x['rating'], reverse=True)

    # Retrieve the top 5 products
    top_rated_products = sorted_products[:5]

    return top_rated_products

def get_average_discounts_by_category():
    category_discounts = defaultdict(list)

    with open('dataset.csv', 'r', encoding='utf-8') as file:
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

    with open('dataset.csv', 'r', encoding='utf-8') as file:
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
