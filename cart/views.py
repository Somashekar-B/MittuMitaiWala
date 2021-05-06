from django.shortcuts import render,redirect,reverse
from .models import CartItems, Address,Orders
from django.db.models import Q
from django.views.generic import ListView,TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from store.models import OilTypes, SpecificTypes, GheeTypes
from random import randint


# Create your views here.

@login_required
def add_to_cart(request):
    user = request.user
    quantity = request.GET.get('qty')
    # print(quantity)
    sweet = request.session['item']
    bp = SpecificTypes.objects.get(type_name=sweet).base_price_per_kilo
    cat = request.session['cat']
    oil = request.session['oil']
    ghee = request.session['ghee']
    oil_add_on = OilTypes.objects.get(oil_name=oil).add_on_per_kilo
    ghee_add_on = GheeTypes.objects.get(ghee_name=ghee).add_on_per_kilo
    amount_per_kilo = bp + oil_add_on + ghee_add_on
    total = float(quantity) * amount_per_kilo
    image = SpecificTypes.objects.get(type_name=sweet).image

    item = CartItems(user=user,
                     quantity=quantity,
                     sweet_name=sweet,
                     category=cat,
                     oil_type=oil,
                     ghee_type=ghee,
                     amount=total,
                     image=image)

    item.save()

    return redirect('user-cart')


def removeCartItem(request, id):
    CartItems.objects.filter(pk=id).delete()
    return redirect('user-cart')


class CartView(LoginRequiredMixin, CreateView, ListView):
    model = Address
    fields = ['first_name','last_name','address_line_1','address_line_2','landmark','city','pincode','phone']
    template_name = 'cart/cart_list.html'
    context_object_name = 'products'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)

        context['products'] = CartItems.objects.filter(Q(user=self.request.user) & Q(is_ordered=False))
        context['count'] = CartItems.objects.filter(Q(user=self.request.user) & Q(is_ordered=False)).count()
        return context


class OrderSummary(TemplateView):
    model = CartItems
    template_name = 'cart/order_summary.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderSummary, self).get_context_data(**kwargs)

        products = CartItems.objects.filter(Q(user=self.request.user) & Q(is_ordered=False))
        total = 0.00

        for item in products:
            total += item.amount

        context['products'] = products
        context['total'] = total
        context['address'] = Address.objects.filter(user=self.request.user).last()
        return context


def setvalues(request):
    order_id = randint(100000000000, 999999999999)
    products = CartItems.objects.filter(Q(user=request.user) & Q(is_ordered=False))

    count=CartItems.objects.filter(order_id=order_id).count()
    print(count)

    while True:
        if count:
            order_id = randint(100000000000, 999999999999)
            count = CartItems.objects.filter(order_id=order_id).count()
        else:
            break

    for item in products:
        item.is_ordered = True
        item.user_diplay = True
        item.order_id = order_id
        item.save()

    address = Address.objects.filter(user=request.user).last()
    address.order_id = order_id
    address.save()
    print(request.user)
    order = Orders(user=request.user,
                   order=order_id)
    order.save()
    return redirect('complete-order')


class CompleteOrder(LoginRequiredMixin, TemplateView):
    model=CartItems
    template_name = 'cart/complete_order.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CompleteOrder, self).get_context_data(**kwargs)
        order_new = Orders.objects.filter(user=self.request.user).last()
        order_id = order_new.order

        items = CartItems.objects.filter(order_id=order_id)
        total=0.00
        for item in items:
            total += item.amount
            item.confirmed = True
            item.save()

        order_new.amount=total
        order_new.confirmed = True
        order_new.save()

        context['order_id'] = order_id
        return context

