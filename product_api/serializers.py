from rest_framework import serializers
from .models import Category, Item, Cart, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Item
        fields = ['id', 'item_name', 'price', 'on_discount', 'discount_price', 'category', 'stock', 'description']

    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     category = Category.objects.create(**category_data)
    #     item = Item.objects.create(category=category, **validated_data)
    #     return item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'created_at', 'updated_at']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'item', 'quantity', 'created_at', 'updated_at']























# class WriteItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = ['item_name', 'price', 'on_discount', 'discount_price', 'category', 'stock', 'description']
#
#
# class ReadItemSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#
#     class Meta:
#         model = Item
#         fields = ['id', 'item_name', 'price', 'on_discount', 'discount_price', 'category', 'stock', 'description']
#         read_only_fields = fields
#
