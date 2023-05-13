from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Product(models.Model):
    store = models.CharField(max_length=100)
    animal = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    product_title = models.CharField(max_length=150)
    # unit_amount = models.FloatField()
    # unit = models.CharField(max_length=10)
    normal_price = models.FloatField()
    sale_price = models.FloatField()
    sale = models.IntegerField()
    age_group = models.CharField(max_length=50, blank=True)
    product_page_url = models.CharField(max_length=100)
    image = models.ImageField(
        default='products/default_product_img.jpg', upload_to='products')
    date_added = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.animal == 'hond' and not self.age_group:
            raise ValidationError(
                {'age_group': 'Age group is required for dogs.'})

    def __str__(self):
        return self.product_title
