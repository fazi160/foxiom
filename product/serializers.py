from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    product_id = serializers.CharField(max_length=20)
    product_name = serializers.CharField(max_length=255)
    category = serializers.ListField(child=serializers.CharField())
    discounted_price = serializers.CharField(max_length=10, allow_null=True)
    actual_price = serializers.CharField(max_length=10, allow_null=True)
    discount_percentage = serializers.CharField(max_length=5, allow_null=True)
    rating = serializers.FloatField(allow_null=True)
    rating_count = serializers.IntegerField(default=0, allow_null=True)
    about_product = serializers.CharField(allow_null=True)
    user_id = serializers.CharField(max_length=100, allow_null=True)
    user_name = serializers.CharField(max_length=100, allow_null=True)
    review_id = serializers.CharField(max_length=20, allow_null=True)
    review_title = serializers.CharField(max_length=255, allow_null=True)
    review_content = serializers.CharField(allow_null=True)
    img_link = serializers.URLField(allow_null=True)
    product_link = serializers.URLField(allow_null=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Remove keys with None values
        data = {key: value for key, value in data.items() if value is not None}
        return data
