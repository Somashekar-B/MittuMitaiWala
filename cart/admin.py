from django.contrib import admin
from .models import Cart, CartItems, Address, Orders

# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Address)
admin.site.register(Orders)
