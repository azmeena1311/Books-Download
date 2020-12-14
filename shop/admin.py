from django.contrib import admin
from shop.models import ProductImages,Product,User,Payment
from django.utils.html import  format_html

# Register your models here.

class ProductImageModel(admin.StackedInline):
    model = ProductImages

class ProductModel(admin.ModelAdmin):
    list_display = ['id','name','get_description','get_price','get_discount', 'get_sale_price','file','thumbnail']
    inlines = [ProductImageModel]

    def get_sale_price(self, obj):
        return f'₹ {((obj.price) - (obj.price * (obj.discount / 100)))}'

    def get_description(self,obj):
        return format_html(f'<span title="{obj.description}">{obj.description[0:15]}...</span>')

    def get_price(self, obj):
        return '₹ ' + str(obj.price)

    def get_discount(self, obj):
        return str(obj.discount) + " %"

    get_sale_price.short_description = "Sale Price"
    get_discount.short_description = "Discount"
    get_price.short_description = "Price"

# admin.site.register(ProductImages,ProductImageModel)

admin.site.register(Product,ProductModel)
admin.site.register(User)
admin.site.register(Payment)
