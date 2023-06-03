from django.contrib import admin

from .models import Color, Size, Product, Order

# Register your models here.
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Order)

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
