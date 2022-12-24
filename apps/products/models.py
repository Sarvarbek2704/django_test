from django.db import models
from apps.common.models import BaseModel


class SaleTypeChoices(BaseModel):
    """
    Choices for SaleType
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductCategory(BaseModel):
    """
    Product Category
    """

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_category', blank=True, null=True)

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    """
    Product Image Object
    """

    image = models.ImageField(upload_to='products/images/')
    alt = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.image.name


class Product(BaseModel):

    """
    Product Model
    """

    title = models.CharField(max_length=255, verbose_name='Mahsulot nomi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narx')
    sold = models.IntegerField(default=0, verbose_name='Sotildi')
    sale_type = models.ManyToManyField(SaleTypeChoices, verbose_name='Sotuv turlari')
    in_stock = models.BooleanField(default=True, verbose_name='Sotuvda bor')
    categories = models.ManyToManyField(ProductCategory, verbose_name='Kategoriyalar')
    images = models.ManyToManyField(ProductImage, verbose_name='Rasmalar')

    def __str__(self):
        return self.title
