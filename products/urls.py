from django.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from products import views

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^products/$', views.ProductList.as_view(), name='product-list'),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='product-detail'),
    url(r'^catalogs/$', views.CatalogList.as_view(), name='catalog-list'),
    url(r'^catalogs/(?P<pk>[0-9]+)/$', views.CatalogDetail.as_view(), name='catalog-detail'),
    url(r'^catalogs/categories/$', views.CatalogCategoryList.as_view(), name='catalogcategory-list'),
    url(r'^catalogs/categories/(?P<pk>[0-9]+)/$', views.CatalogCategoryDetail.as_view(),
        name='catalogcategory-detail'),
])


# Login and logout views for the browse API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
