from django.urls import include, path
from rest_framework import routers
from .views import (
    CategoryViewSet,
    ItemViewSet,
    CartView,
    # ReduceCartView,
)

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename="category")
router.register(r'product', ItemViewSet, basename="product")

urlpatterns = [
    path('', include(router.urls)),
    path('cart-view/<int:pk>/', CartView.as_view(), name='cart-view'),
    # path('reduce-cart/<int:pk>/', ReduceCartView.as_view(), name='reduce-cartw'),

]
