from django.contrib import admin
from .models import SweetType, SpecificTypes, GheeTypes, OilTypes, Contact;
# SweetCategory

# Register your models here.
admin.site.register(SweetType)
# admin.site.register(SweetCategory)
admin.site.register(Contact)
admin.site.register(SpecificTypes)
admin.site.register(OilTypes)
admin.site.register(GheeTypes)
