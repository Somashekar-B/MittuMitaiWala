from django.urls import path
from .views import CartView, add_to_cart,OrderSummary,CompleteOrder,setvalues, removeCartItem


urlpatterns = [
    path('item/add/', add_to_cart, name='add-cart'),
    path('remove-item/<int:id>',removeCartItem,name='remove-item'),
    path('order-summary/', OrderSummary.as_view(), name='summary'),
    path('cart/items', CartView.as_view(), name='user-cart'),
    path('order-complete/', CompleteOrder.as_view(), name='complete-order'),
    path('set-values/',setvalues,name='set-values')

]
