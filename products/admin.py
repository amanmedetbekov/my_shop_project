from django.contrib import admin
from .models import Category, Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'description', 'price', 'image', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Product
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Comment)


# admin.site.register(Category)
# admin.site.register(ProductAdmin)
