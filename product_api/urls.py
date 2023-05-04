from django.urls import include, path
from rest_framework import routers
from .views import (
    CategoryViewSet,
    ItemViewSet,
    AddToCartView,
)

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename="category")
router.register(r'product', ItemViewSet, basename="product")

urlpatterns = [
    path('', include(router.urls)),
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add-to-cart'),

]
