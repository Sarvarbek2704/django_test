from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from apps.products.filterset import ProductFilter

from apps.products.models import Product, ProductCategory
from apps.products.serializers import ProductCategorySerializer, ProductSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['sale_type', 'in_stock']
    search_fields = ['title']
    ordering_fields = '__all__'
    filterset_class = ProductFilter


class ProductCategoriesList(ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
