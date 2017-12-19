from products.models import Product, CatalogCategory, Catalog, ProductAttributeValue

from rest_framework import serializers


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    attribute = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = ProductAttributeValue
        fields = ('attribute', 'value')


class ProductSerializer(serializers.ModelSerializer):
    details = ProductAttributeValueSerializer(many=True, read_only=True)

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
