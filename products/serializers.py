from products.models import Product, CatalogCategory, Catalog, ProductAttributeValue

from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()

    def get_details(self, product):
        attributes_value = ProductAttributeValue.objects.filter(product=product)
        details = {}
        for attribute in attributes_value:
            details[attribute.attribute.name] = attribute.value
        return details

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'quantity', 'details')
        read_only_fields = ('id',)


class CatalogCategorySerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = CatalogCategory
        fields = ('id', 'name', 'slug', 'parent', 'description', 'catalog', 'products')
        read_only_fields = ('id',)


class CatalogSerializer(serializers.ModelSerializer):
    categories = serializers.HyperlinkedRelatedField(many=True, view_name='catalogcategory-detail', read_only=True)

    class Meta:
        model = Catalog
        fields = ('id', 'name', 'categories')
        read_only_fields = ('id',)
