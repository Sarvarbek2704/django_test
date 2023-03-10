# Generated by Django 4.0.5 on 2022-06-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaleTypeChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Mahsulot nomi')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Narx')),
                ('sold', models.IntegerField(default=0, verbose_name='Sotildi')),
                ('in_stock', models.BooleanField(default=True, verbose_name='Sotuvda bor')),
                ('sale_type', models.ManyToManyField(to='products.saletypechoices', verbose_name='Sotuv turlari')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
