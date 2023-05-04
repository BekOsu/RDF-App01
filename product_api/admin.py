from django.contrib import admin
from .models import (
    Item,
    Category,
    OrderItem,
    Order,
)

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
