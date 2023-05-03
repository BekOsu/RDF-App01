from rest_framework import viewsets, filters
from .models import Category, Item, User, Cart
from .serializers import (
    CategorySerializer, ItemSerializer, UserSerializer, CartSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all().order_by('category_id')
    serializer_class = ItemSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("item_name",)
    ordering_fields = ("price", "stock")

    # def get_serializer_class(self):
    #     if self.action in ("list", "retrieve"):
    #         return ReadItemSerializer
    #     return WriteItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer
