from django.contrib import admin
from .models import Material,Item,Order
# Register your models here.
admin.site.register(Material)
admin.site.register(Item)
admin.site.register(Order)