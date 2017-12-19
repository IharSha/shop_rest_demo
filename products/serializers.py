from products.models import Product, CatalogCategory, Catalog, ProductAttributeValue

from rest_framework import serializers


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    attribute = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = ProductAttributeValue
        fields = ('attribute', 'value')


class ProductSerializer(serializers.ModelSerializer):
    details = ProductAttributeValueSerializer(many=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'quantity', 'details')

    def create(self, validated_data):
        attribute_data = validated_data.pop('details')
        product = Product.objects.create(**validated_data)
        for attribute_value in attribute_data:
            value = attribute_value.get('value')
            ProductAttributeValue.objects.create(product=product,
                                                 attribute=attribute_value.get('attribute'),
                                                 value=value)
        return product

    def update(self, product, validated_data):
        attribute_data = validated_data.pop('details')
        product.name = validated_data.get('name', product.name)
        product.category = validated_data.get('category', product.category)
        product.price = validated_data.get('price', product.price)
        product.quantity = validated_data.get('quantity', product.quantity)
        product.save()

        ProductAttributeValue.objects.filter(product=product).delete()  # clear prv data
        for attribute_value in attribute_data:
            value = attribute_value.get('value')

            product_details, _ = ProductAttributeValue.objects.get_or_create(product=product,
                                                                             attribute=attribute_value.get('attribute'))
            product_details.value = value
            product_details.save()
        return product


class CatalogCategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    catalog = serializers.StringRelatedField()

    class Meta:
        model = CatalogCategory
        fields = ('url', 'id', 'name', 'parent', 'slug', 'description', 'catalog', 'products')


class CatalogSerializer(serializers.ModelSerializer):
    categories = serializers.HyperlinkedRelatedField(many=True, view_name='catalogcategory-detail', read_only=True)

    class Meta:
        model = Catalog
        fields = ('id', 'name', 'categories')
        read_only_fields = ('id',)
