from rest_framework import serializers
from .models import Category, Item, OrderItem, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'price', 'on_discount', 'discount_price', 'category', 'stock', 'description']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    ordered_date = serializers.ReadOnlyField(source='item.ordered_date')
    quantity = serializers.ReadOnlyField(source='item.quantity')

    class Meta:
        model = Order
        fields = '__all__'
