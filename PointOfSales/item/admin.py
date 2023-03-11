from django.contrib import admin
from .models import item, order, item_order
# Register your models here.
admin.site.register(item)
admin.site.register(order)
admin.site.register(item_order)
