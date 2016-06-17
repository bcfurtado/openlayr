from rest_framework import serializers
from api.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category')

    def get_category(self, obj):
        return obj.category_name

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
