from products.models import Product, Catalog, CatalogCategory
from products.serializers import ProductSerializer, CatalogSerializer, CatalogCategorySerializer

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'catalogs': reverse('catalog-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'categories': reverse('catalogcategory-list', request=request, format=format)
    })


class CatalogList(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class CatalogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class CatalogCategoryList(generics.ListCreateAPIView):
    queryset = CatalogCategory.objects.all()
    serializer_class = CatalogCategorySerializer


class CatalogCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatalogCategory.objects.all()
    serializer_class = CatalogCategorySerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
