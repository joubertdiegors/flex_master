# Generated by Django 4.2.13 on 2024-08-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]