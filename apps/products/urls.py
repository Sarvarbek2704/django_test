from django.urls import path

from apps.products.views import ProductCategoriesList, ProductListCreateView


urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product_list_create'),
    path('categories/', ProductCategoriesList.as_view(), name='product_categories_list'),
]
