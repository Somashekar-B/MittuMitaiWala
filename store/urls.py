from django.urls import path
from .views import (
    home,about, ContactUs,
    TypeCreate, TypeUpdate, TypeListView, TypeDelete,
    SweetCreate, SweetUpdate, SweetsCategorised, SweetList, SweetDelete,
    OilCreate, OilUpdate, OilList, OilDelete,
    GheeCreate, GheeUpdate, GheeList, GheeDelete,
    AllList, ItemTable,

    UserStoreTypeView, UserStoreSweetView, UserStoreOilView, UserStoreGheeView,
    completeview, DueView, delivered, UserOrderInfo, DeliverList, deleteDelivered,
    cancelOrder, CancelledOrders, check_cancelled_orders,
    )

urlpatterns = [
    path('', home, name='store-home'),
    path('contact/', ContactUs.as_view(), name="contact"),
    path('new/type/', TypeCreate.as_view(), name='new-type'),
    path('type/<str:slug>/update/', TypeUpdate.as_view(), name='type-update'),
    path('type/all/', TypeListView.as_view(), name='type-all'),
    path('type/<slug:slug>/delete',  TypeDelete.as_view(), name='type-delete'),

    path('new/sweet/', SweetCreate.as_view(), name='new-sweet'),
    path('sweet/<int:pk>/update/', SweetUpdate.as_view(), name='sweet-update'),
    path('sweet/all/', SweetList.as_view(), name='sweet-all'),
    path('sweet/<slug:slug>/delete',  SweetDelete.as_view(), name='sweet-delete'),
    path('sweet/<slug:slug>/', SweetsCategorised.as_view(), name='sweet-cat'),

    path('new/oil/', OilCreate.as_view(), name='new-oil'),
    path('oil/<int:pk>/update/', OilUpdate.as_view(), name='oil-update'),
    path('oil/<slug:slug>/delete',  OilDelete.as_view(), name='oil-delete'),
    path('oils/all/',OilList.as_view(), name='oil-all'),

    path('new/ghee/', GheeCreate.as_view(), name='new-ghee'),
    path('ghee/<int:pk>/update/', GheeUpdate.as_view(), name='ghee-update'),
    path('ghee/<slug:slug>/delete',  GheeDelete.as_view(), name='ghee-delete'),
    path('ghee/all/',GheeList.as_view(), name='ghee-all'),

    path('items/all/',AllList.as_view(), name='items-all'),
    path('items-table/',ItemTable.as_view(), name='items-table'),

    path('store/type/', UserStoreTypeView.as_view(), name='store-type'),
    path('due-list/', DueView.as_view(), name='due-list'),
    path('order-delivered/<int:order_id>', delivered, name='order-delivered'),
    path('store/<str:sweet>/oil/', UserStoreOilView.as_view(), name='store-oil'),
    path('store/<str:oil>/ghee/', UserStoreGheeView.as_view(), name='store-ghee'),
    path('item/<str:ghee>/complete/', completeview, name='item-complete'),
    path('store/<str:cat>/', UserStoreSweetView.as_view(), name='store-sweet'),

    path('your-orders/', UserOrderInfo.as_view(), name='user-orders'),
    path('orders-delivered/', DeliverList.as_view(), name='deliver-list'),
    path('delivery-delete/<int:order_id>', deleteDelivered, name='delete-delivery'),
    path('cancel-order/<int:order_id>/<int:id>/', cancelOrder, name='cancel-order'),
    path('all-cancelled-orders/', CancelledOrders.as_view(), name='cancelled-orders'),
    path('check-cancelled-orders/<int:order_id>/<int:item_id>/', check_cancelled_orders, name='check-cancelled-orders'),
]


