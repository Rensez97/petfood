# Generated by Django 4.1.7 on 2023-03-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='testimages.jpg', upload_to='products'),
        ),
    ]
