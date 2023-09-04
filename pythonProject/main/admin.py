from django.contrib import admin
from main.models import Product, Category, Basket
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price', 'cat',)

class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity']
    extra = 0
admin.site.register(Category, CatAdmin)
admin.site.register(Basket)
# Register your models here.
