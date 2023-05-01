from rest_framework import viewsets
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
    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadItemSerializer
        return WriteItemSerializer
