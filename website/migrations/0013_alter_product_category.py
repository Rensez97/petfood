# Generated by Django 4.1.7 on 2023-04-07 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_remove_product_unit_remove_product_unit_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]
