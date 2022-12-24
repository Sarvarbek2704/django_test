# Generated by Django 4.0.5 on 2022-06-09 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productcategory_productimage_product_categories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_category'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='alt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]