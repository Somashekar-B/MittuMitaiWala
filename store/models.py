from django.db import models
from django.utils import timezone
from PIL import Image
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()


    def get_absolute_url(self):
        return reverse('store-home')

class SweetType(models.Model):
    sweet_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='Sweet_Types',default='default_sweet.jpg')
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('sweet_name','slug')

    def __str__(self):
        return self.sweet_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if(img.height > 300 or img.width > 300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('new-type')

    @property
    def count(request):
        return SweetType.objects.all().count()

    @property
    def varieties(request):
        count = SpecificTypes.objects.filter(sweet_category_id = request.id).count()
        return count


class SpecificTypes(models.Model):
    type_name = models.CharField(max_length=200)
    base_price_per_kilo = models.FloatField()
    slug = models.SlugField(unique=True)
    img_path = 'Sweets'
    image = models.ImageField(upload_to=img_path,default='default_sweet.jpg')
    sweet_category = models.ForeignKey(SweetType, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('type_name','slug')

    def __str__(self):
        return self.type_name

    def save(self,*args ,**kwargs):
        super().save(*args ,**kwargs)

        img = Image.open(self.image.path)

        if(img.height > 300 or img.width > 300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('new-sweet')

    @property
    def count(request):
        return SpecificTypes.objects.all().count()

    @property
    def varieties(request):
        count = SpecificTypes.objects.get(pk=request.id).sweet_category
        return count


class OilTypes(models.Model):
    oil_name = models.CharField(max_length=200)
    add_on_per_kilo = models.FloatField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='OilTypes',default='default_oil.jpg')
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('oil_name','slug')
    def __str__(self):
        return self.oil_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if (img.height > 300 or img.width > 300):
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('new-oil')

    @property
    def count(request):
        return OilTypes.objects.all().count()


class GheeTypes(models.Model):
    ghee_name = models.CharField(max_length=200)
    add_on_per_kilo = models.FloatField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='GheeTypes',default='default_ghee.jpg')
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('ghee_name','slug')

    def __str__(self):
        return self.ghee_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if (img.height > 300 or img.width > 300):
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('new-ghee')

    @property
    def count(request):
        return GheeTypes.objects.all().count()
