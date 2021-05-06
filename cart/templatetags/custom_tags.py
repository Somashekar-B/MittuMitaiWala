from django import template
from cart.models import CartItems, Address
from django.db.models import Q

register = template.Library()


@register.simple_tag
def get_orders_total(order_id):
    objects = CartItems.objects.filter(order_id=order_id)
    total=0.00

    for item in objects:
        total+=item.amount

    return total


@register.simple_tag
def get_cancelled_total(order_id):
    objects = CartItems.objects.filter(Q(order_id=order_id) & Q(is_canceled=True))
    total=0.00

    for item in objects:
        total+=item.amount

    return total


@register.simple_tag
def get_address(order_id):
    return Address.objects.filter(order_id=order_id).last()