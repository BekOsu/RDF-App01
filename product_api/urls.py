from django.urls import include, path
from rest_framework import routers

from .import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ItemViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
