# Generated by Django 4.1.7 on 2023-03-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50)),
                ('product_title', models.CharField(max_length=50)),
                ('product_page_url', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=100)),
                ('unit', models.IntegerField()),
                ('normal_price', models.IntegerField()),
                ('sale_price', models.IntegerField()),
                ('food_group', models.CharField(max_length=50)),
                ('age_group', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
