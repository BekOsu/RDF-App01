from rest_framework import viewsets, filters, generics
from rest_framework.response import Response
from .models import Category, Item, OrderItem, Order
from django.shortcuts import get_object_or_404
from django.utils import timezone
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


class AddToCartView(generics.GenericAPIView):
    serializer_class = OrderItemSerializer

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
                order_item.quantity += 1
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
