from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView, UpdateView, ListView, RedirectView, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import SpecificTypes, SweetType, OilTypes, GheeTypes,Contact
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from cart.models import CartItems,Orders
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,'store/home.html');

def about(request):
    return render(request,'users/about.html');

class ContactUs(CreateView, SuccessMessageMixin):
    model = Contact
    fields = ['name', 'email', 'content']
    template_name = 'store/contact.html'

    def form_valid(self, form):
        body = "Name: "+ form.instance.name + "\nEmail Id: "+ form.instance.email+"\n Message : \n"+form.instance.content
        send_mail("MittuMitaiwala Site", body, "myhobbyprojects80@gmail.com", ["myhobbyprojects80@gmail.com"],fail_silently=False);
        send_mail("Bakery Website", "Thanks you so much for your valuable Response, it will help us get better", "myhobbyprojects80@gmail.com", [form.instance.email],fail_silently=False)
        return super().form_valid(form)

    success_message = "Thank You for the valuable Response..!"

def error_404_view(request, exception):
    print("jhgjj");
    return render(request, 'store/404.html')


class TypeCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = ('is_superuser')
    model = SweetType
    fields = ['sweet_name', 'slug', 'image']
    template_name = 'store/type_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    success_message = "Sweet Category Created Successfully..!!!"


class TypeUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = ('is_superuser')
    model = SweetType
    fields = ['sweet_name','slug','image']

    def form_valid(self, form):
        return super().form_valid(form)

    success_message = "Sweet Category Updated Successfully..!!!!"

    def get_success_url(self):
        return reverse('type-all')


class TypeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'is_superuser'
    model = SweetType

    def get_queryset(self):
        query = self.kwargs['slug']
        if query:
            object_list = self.model.objects.filter(slug=query)
            return object_list

    def get_success_url(self):
        return reverse('type-all')

class SweetCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = ('is_superuser')
    model = SpecificTypes
    fields = ['sweet_category','type_name','slug','image','base_price_per_kilo']

    def form_valid(self, form):
        return super().form_valid(form)


class SweetUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = ('is_superuser')
    model = SpecificTypes
    fields = ['sweet_category','type_name','slug','image','base_price_per_kilo']

    def form_valid(self, form):
        return super().form_valid(form)


class SweetDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'is_superuser'
    model = SpecificTypes

    def get_queryset(self):
        query = self.kwargs['slug']
        if query:
            object_list = self.model.objects.filter(slug=query)
            return object_list

    def get_success_url(self):
        return reverse('sweet-all')


class OilCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = ('is_superuser')
    model = OilTypes
    fields = ['oil_name','slug','image','add_on_per_kilo']

    def form_valid(self, form):
        return super().form_valid(form)


class OilUpdate(LoginRequiredMixin,PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = ('is_superuser')
    model = OilTypes
    fields = ['oil_name','slug','image','add_on_per_kilo']

    def form_valid(self, form):
        return super().form_valid(form)


class OilDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'is_superuser'
    model = OilTypes

    def get_queryset(self):
        query = self.kwargs['slug']
        if query:
            object_list = self.model.objects.filter(slug=query)
            return object_list

    def get_success_url(self):
        return reverse('oil-all')


class GheeCreate(LoginRequiredMixin,PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = ('is_superuser')
    model = GheeTypes
    fields = ['ghee_name','slug','image','add_on_per_kilo']

    def form_valid(self, form):
        return super().form_valid(form)


class GheeUpdate(LoginRequiredMixin,PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = ('is_superuser')
    model = GheeTypes
    fields = ['ghee_name','slug','image','add_on_per_kilo']

    def form_valid(self, form):
        return super().form_valid(form)


class GheeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'is_superuser'
    model = GheeTypes

    def get_queryset(self):
        query = self.kwargs['slug']
        if query:
            object_list = self.model.objects.filter(slug=query)
            return object_list

    def get_success_url(self):
        return reverse('ghee-all')


class TypeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'is_superuser'
    model = SweetType
    template_name = 'store/type_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TypeListView, self).get_context_data(**kwargs)
        type = SweetType.objects.all().order_by("-date")
        paginator = Paginator(type,self.paginate_by)
        self.request.session['prev_url'] = self.request.META.get('HTTP_REFERER')
        page = self.request.GET.get('page')

        try:
            type = paginator.page(page)
        except PageNotAnInteger:
            type = paginator.page(1)
        except EmptyPage:
            type = paginator.page(paginator.num_pages)
            
        context['type'] = type

        return context


class SweetList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'is_superuser'
    model = SpecificTypes
    template_name = 'store/sweets_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SweetList, self).get_context_data(**kwargs)
        sweets = SpecificTypes.objects.all().order_by("-date")
        paginator = Paginator(sweets, self.paginate_by)
        self.request.session['prev_url'] = self.request.META.get('HTTP_REFERER')
        page = self.request.GET.get('page')

        try:
            sweets = paginator.page(page)
        except PageNotAnInteger:
            sweets = paginator.page(1)
        except EmptyPage:
            sweets = paginator.page(paginator.num_pages)

        context['sweets'] = sweets

        return context


class OilList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'is_superuser'
    model = OilTypes
    template_name = 'store/oils_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(OilList, self).get_context_data(**kwargs)
        oils = OilTypes.objects.all().order_by("-date")
        paginator = Paginator(oils, self.paginate_by)
        self.request.session['prev_url'] = self.request.META.get('HTTP_REFERER')
        page = self.request.GET.get('page')

        try:
            oils = paginator.page(page)
        except PageNotAnInteger:
            oils = paginator.page(1)
        except EmptyPage:
            oils = paginator.page(paginator.num_pages)

        context['oils'] = oils

        return context


class GheeList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'is_superuser'
    model = GheeTypes
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(GheeList, self).get_context_data(**kwargs)
        ghee = GheeTypes.objects.all().order_by("-date")
        paginator = Paginator(ghee, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            ghee = paginator.page(page)
        except PageNotAnInteger:
            ghee = paginator.page(1)
        except EmptyPage:
            ghee = paginator.page(paginator.num_pages)

        self.request.session['prev_url'] = self.request.META.get('HTTP_REFERER')

        context['ghee'] = ghee
        context['prev_url'] = self.request.session['prev_url']
        print(context['prev_url'])

        return context


class SweetsCategorised(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'is_superuser'
    model = SpecificTypes

    def get_context_data(self, **kwargs):
        context = super(SweetsCategorised, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        item = SweetType.objects.get(slug=slug).id
        context['sweets'] = SpecificTypes.objects.filter(sweet_category_id=item).order_by("-date")
        context['category'] = SweetType.objects.get(slug=slug)
        return context


class AllList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'is_superuser'
    model = SweetType
    template_name = 'store/all_list.html'

    def get_context_data(self, **kwargs):
        self.request.session['prev_url'] = self.request.META.get('HTTP_REFERER')
        context = super(AllList, self).get_context_data(**kwargs)

        context['type'] = SweetType.objects.all().order_by("-date")
        context['sweets'] = SpecificTypes.objects.all().order_by("-date")
        context['oils'] = OilTypes.objects.all().order_by("-date")
        context['ghee'] = GheeTypes.objects.all().order_by("-date")

        return context


class ItemTable(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = 'is_superuser'
    model = SweetType
    template_name = 'store/items_table.html'

    def get_context_data(self, **kwargs):
        context = super(ItemTable, self).get_context_data(**kwargs)

        context['type'] = SweetType.objects.all().order_by("-date")
        context['sweets'] = SpecificTypes.objects.all().order_by("-date")
        context['oils'] = OilTypes.objects.all().order_by("-date")
        context['ghee'] = GheeTypes.objects.all().order_by("-date")

        return context


class DueView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'is_superuser'
    model = CartItems
    template_name = 'store/due_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(DueView, self).get_context_data(**kwargs)

        items = CartItems.objects.filter(Q(is_ordered=True) & Q(is_delivered=False) & Q(is_canceled=False))
        orders = Orders.objects.filter(Q(is_delivered=False) & Q(is_canceled=False))
        count = Orders.objects.filter(is_delivered=False).count()
        paginator = Paginator(orders, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            orders = paginator.page(page)
        except PageNotAnInteger:
            orders = paginator.page(1)
        except EmptyPage:
            orders = paginator.page(paginator.num_pages)

        context['orders'] = orders
        context['items'] = items
        context['count'] = count
        return context


def delivered(request,order_id):
    items = CartItems.objects.filter(order_id=order_id)
    order = Orders.objects.get(order=order_id)

    for item in items:
        item.is_delivered = True
        item.delivered_on = timezone.now()
        item.save()

    order.is_delivered = True
    order.delivered_on = timezone.now()
    order.save()

    messages.success(request, "Order Has been added to Delivered list")
    return redirect('due-list')


def deleteDelivered(request, order_id):
    Orders.objects.filter(order=order_id).delete();
    messages.success(request, "Delivery Entry has been deleted")
    return redirect('deliver-list');

class DeliverList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "is_superuser"
    model = CartItems
    template_name = 'store/delivered_list.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DeliverList, self).get_context_data(**kwargs)

        items = CartItems.objects.filter(is_delivered=True).order_by("-added_on")
        order = Orders.objects.filter(is_delivered=True).order_by("-date")
        count = Orders.objects.filter(is_delivered=True).count()

        context['count'] = count
        context['orders'] = order
        context['items'] = items

        return context


class CancelledOrders(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'is_superuser'
    model = CartItems
    template_name = 'store/cancelled_orders.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CancelledOrders, self).get_context_data(**kwargs)
        context['orders'] = Orders.objects.filter(Q(is_itemcancelled = True) & Q(is_complete_cancelled=False))
        context['items'] = CartItems.objects.filter(Q(is_canceled=True) & Q(is_checked=False))
        context['count'] = CartItems.objects.filter(Q(is_canceled=True) & Q(is_checked=False)).count()
        print(context['count'])

        return context


def check_cancelled_orders(request,order_id,item_id):
    order = Orders.objects.get(order=order_id)
    if item_id > 0:
        item = CartItems.objects.get(id=item_id)
        item.is_checked = True
        item.save()

    else:
        items = CartItems.objects.filter(Q(order_id=order_id) & Q(is_canceled=True))
        items_count = CartItems.objects.filter(Q(order_id=order_id) & Q(is_canceled=True)).count()
        all_items = CartItems.objects.filter(Q(order_id=order_id)).count()
        for item in items:
            item.is_checked = True
            item.save()

        if items_count == all_items:
            order.is_complete_cancelled = True
            order.save()

    return redirect('cancelled-orders')



class UserOrderInfo(LoginRequiredMixin, ListView):
    model = CartItems
    template_name = 'store/user_order_list.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserOrderInfo, self).get_context_data(**kwargs)

        items = CartItems.objects.filter(Q(user=self.request.user) & Q(is_canceled=False)).order_by("-added_on")
        present_count = CartItems.objects.filter(Q(user=self.request.user) & Q(is_canceled=False)).count()
        deliver_count = CartItems.objects.filter(Q(user=self.request.user) & Q(is_delivered=True)).count()
        total_count = CartItems.objects.filter(Q(user=self.request.user)).count()
        context['items'] = items
        context['present_count'] = present_count
        context['total_count'] = total_count
        context['deliver_count'] = deliver_count

        return context


def cancelOrder(request,order_id, id):
    item = CartItems.objects.get(id=id)
    item.is_canceled = True
    item.save()

    order=Orders.objects.get(order=order_id)
    order_items = CartItems.objects.filter(order_id=order_id)

    if order.is_itemcancelled == False:
        order.is_itemcancelled = True
        order.save()

    flag = 0
    for item in order_items:
        if item.is_canceled == False:
            flag=1
            break

    if flag == 0:
        order.is_canceled = True
        order.save()

    return redirect('user-orders')


""" 
    Start of real store for user / customer interaction and purchase
    it consists of item display pages and a final product page 
    and a user specific cart for adding items and for purchase which demands user login     
"""


class UserStoreTypeView(ListView):
    model = SweetType
    context_object_name = 'types'
    template_name = 'store/user_store_type.html'

    def get_queryset(self):

        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(sweet_name__icontains = query)
        else:
            object_list = self.model.objects.all()
        return object_list


class UserStoreSweetView(ListView):
    model = SpecificTypes
    template_name = 'store/user_store_sweet.html'
    context_object_name = 'sweets'

    def get_queryset(self, **kwargs):
        cat = self.kwargs['cat']
        self.request.session['cat'] = cat
        item = SweetType.objects.get(sweet_name=cat)
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(Q(sweet_category_id=item.id) & Q(type_name__icontains = query)).order_by("-date")
        else:
            object_list = self.model.objects.filter(sweet_category_id=item.id).order_by("-date")
        return object_list


class UserStoreOilView(ListView):
    model = OilTypes
    context_object_name = 'oils'
    template_name = 'store/user_store_oil.html'

    def get_queryset(self):
        sweet = self.kwargs['sweet']
        self.request.session['item'] = sweet
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(oil_name__icontains = query)
        else:
            object_list = self.model.objects.all()
        return object_list


class UserStoreGheeView(ListView):
    model = GheeTypes
    context_object_name = 'ghee'
    template_name = 'store/user_store_ghee.html'

    def get_queryset(self):
        oil = self.kwargs['oil']
        self.request.session['oil'] = oil
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(oil_name__icontains = query)
        else:
            object_list = self.model.objects.all()
        return object_list


def completeview(request,ghee):
    request.session['ghee'] = ghee
    sweet = request.session['item']
    cat = request.session['cat']
    bp = SpecificTypes.objects.get(type_name = sweet).base_price_per_kilo
    image = SpecificTypes.objects.get(type_name = sweet).image.url
    oil = request.session['oil']
    oil_add_on = OilTypes.objects.get(oil_name = oil).add_on_per_kilo
    ghee_add_on = GheeTypes.objects.get(ghee_name=ghee).add_on_per_kilo
    total = bp + oil_add_on + ghee_add_on

    request.session['price'] = total

    count = CartItems.objects.filter(Q(sweet_name=request.session['item']) &
                                     Q(category=request.session['cat']) &
                                     Q(oil_type=request.session['oil']) &
                                     Q(ghee_type=request.session['ghee']) &
                                     Q(is_ordered=False)).count()
    print(count)
    context = {
        'sweet' : sweet,
        'image' : image,
        'cat' : cat,
        'oil' : oil,
        'ghee' : ghee,
        'total' : total,
        'count':count
    }

    return render(request,'store/complete.html',context)









