# Generated by Django 5.0.6 on 2024-05-10 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_attribute_category_parent_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ManyToManyField(related_name='product_type', to='catalogue.producttype'),
        ),
        migrations.AddField(
            model_name='productline',
            name='attribute',
            field=models.ManyToManyField(related_name='attribute', to='catalogue.attribute'),
        ),
    ]