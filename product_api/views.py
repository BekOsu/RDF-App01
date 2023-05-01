from rest_framework import viewsets, filters
from .models import Category, Item
from .serializers import CategorySerializer, ReadItemSerializer, WriteItemSerializer


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
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("item_name",)
    ordering_fields = ("price", "stock")

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadItemSerializer
        return WriteItemSerializer
