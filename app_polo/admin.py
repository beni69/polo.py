from django.contrib import admin

from .models import Color, Size, Product, Order, Class, PoloUser

# Register your models here.
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(Class)
admin.site.register(PoloUser)

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
