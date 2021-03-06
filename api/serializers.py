from rest_framework import serializers
from api.models import Product, Category, Order

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category')

    def get_category(self, obj):
        return obj.category.name

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

class OrderSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', required=False)

    class Meta:
        model = Order
        fields = ('id', 'name', 'email', 'address', 'products', 'status', 'created_at')
