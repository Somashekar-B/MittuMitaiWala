from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile
from PIL import Image
from django.utils import timezone

# Create your models here.


class CartItems(models.Model):
    order_id = models.BigIntegerField(null=True)
    user = models.CharField(max_length=100, null=True)
    sweet_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    oil_type = models.CharField(max_length=100 )
    ghee_type = models.CharField(max_length=100 )
    quantity = models.FloatField(default=1)
    amount = models.FloatField(max_length=20,default=0.00)
    image = models.ImageField(upload_to='Sweet_Types')
    confirmed = models.BooleanField(default=False)
    is_ordered = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    user_display = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now=True)
    delivered_on = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.sweet_name

    class Meta:
        unique_together = ('user','sweet_name', 'category', 'oil_type', 'ghee_type', 'order_id', 'is_ordered')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)




class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItems)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    def get_cart_items(self):
        return self.items.all()

    def __str__(self):
        return self.user.username

    @property
    def varieties(self,ord_id):
        count=CartItems.objects.filter(order_id=ord_id).count()
        return count



class Address(models.Model):
    order_id = models.BigIntegerField(null=True)
    whether_added = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    pincode = models.IntegerField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)



    def __str__(self):
        return f'{self.user} address'

    def get_absolute_url(self):
        return reverse('summary')


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.BigIntegerField(null=True)
    amount = models.FloatField(max_length=20, default=0.00)
    date = models.DateTimeField(default=timezone.now())
    confirmed = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    is_itemcancelled = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)
    is_complete_cancelled = models.BooleanField(default=False)
    delivered_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.user} Orders'
