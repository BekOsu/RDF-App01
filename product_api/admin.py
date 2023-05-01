from django.contrib import admin
from .models import (
    Item,
    Category,

)

admin.site.register(Category)
admin.site.register(Item)

