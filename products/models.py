from django.db import models
from datetime import datetime


class Product(models.Model):
    category = models.ForeignKey('CatalogCategory', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='product_photo', blank=True)
    manufacturer = models.CharField(max_length=300, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Catalog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class CatalogCategory(models.Model):
    """
    The "CatalogCategory" model creates a relationship to our
    "Catalog" model and connection between "Catalog" and "Product"
    also possible to create category hierarchies with "parent" field.
    """
    catalog = models.ForeignKey('Catalog', related_name='categories', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Catalog categories"

    def __str__(self):
        if self.parent:
            return '{0}: {1} - {2}'.format(self.catalog.name, self.parent.name, self.name)
        return '{0}: {1}'.format(self.catalog.name, self.name)


class ProductAttribute(models.Model):
    """
    The "ProductAttribute" model represents a class of feature found
    across a set of products. It describes what kind of a
    product feature we are trying to capture. Possible attributes
    include things such as materials, colors, sizes, and many, many
    more.
    """
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    """
    The "ProductAttributeValue" model represents information unique to a
    specific product. This is a generic design that can be used
    to extend the information contained in the "Product" model with
    specific, extra details.
    """
    product = models.ForeignKey('Product', related_name='details', on_delete=models.CASCADE)
    attribute = models.ForeignKey('ProductAttribute', on_delete=models.CASCADE)
    value = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("product", "attribute")

    def __str__(self):
        return '{0}: {1}: {2}'.format(self.product, self.attribute, self.value)

