from rest_framework import viewsets, filters, generics, status
from rest_framework.response import Response
from .models import Category, Item, OrderItem, Order
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .serializers import (
    CategorySerializer, ItemSerializer, OrderItemSerializer, OrderSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.select_related("category")
    serializer_class = ItemSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("item_name",)
    ordering_fields = ("price", "stock")


class CartView(generics.GenericAPIView):
    serializer_class = OrderItemSerializer

    def get_object(self, pk):
        order = Order.objects.filter(user=self.request.user, ordered=False).first()
        if order:
            order_item = get_object_or_404(OrderItem, order=order, item__pk=pk, ordered=False)
            return order_item
        return None

    def get_object(self, pk):
        order_qs = Order.objects.filter(user=self.request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            order_item_qs = order.items.filter(item__pk=pk)
            if order_item_qs.exists():
                return order_item_qs[0]
        return None

    def post(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False
        )
        order_qs = Order.objects.filter(user=request.user, ordered=False)

        if order_qs.exists():
            order = order_qs[0]

            if order.items.filter(item__pk=item.pk).exists():

                order_item.save()
                serializer = OrderSerializer(order)
                return Response(serializer.data)
            else:
                order.items.add(order_item)
                serializer = OrderSerializer(order)
                return Response(serializer.data)
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            serializer = OrderSerializer(order)
            return Response(serializer.data)

    def delete(self, request, pk, format=None):

        item = get_object_or_404(Item, pk=pk)
        order_qs = Order.objects.filter(user=request.user, ordered=False)

        if order_qs.exists():
            order = order_qs[0]

            if order.items.filter(item__pk=item.pk).exists():
                order_item = OrderItem.objects.filter(
                    item=item,
                    user=request.user,
                    ordered=False
                )[0]
                order_item.delete()
                serializer = OrderSerializer(order)
                messages.info(request, "Item \"" + order_item.item.item_name + "\" removed from your cart")
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                messages.info(request, "This item is not in your cart")
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            messages.info(request, "You do not have an order")
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        order_item = self.get_object(pk)
        if order_item is not None:
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            message = f"Item quantity was updated for {order_item.item.item_name}"
            return Response({'message': message})
        else:
            message = f"This Item is not in your cart"
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)

