from django.contrib import admin
from .models import Product, ProductAttribute, ProductAttributeValue, Catalog, CatalogCategory


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    fields = ('attribute', 'value', 'description')

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductAttributeValueInline,)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute)
admin.site.register(Catalog)
admin.site.register(CatalogCategory)
