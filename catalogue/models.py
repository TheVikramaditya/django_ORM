from django.db import models
import uuid
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    pid = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    is_digital = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True,editable=False)#date time will not update , but only created for first time
    upted_at = models.DateTimeField(auto_now=True,editable=False)
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.name
    
class ProductLine(models.Model):
    price = models.DecimalField(max_digits=8,decimal_places=2)
    sku = models.UUIDField(default=uuid.uuid4)
    stock_qty = models.IntegerField()
    order = models.IntegerField()
    weight = models.FloatField()
    

class ProductImage(models.Model):
    name = models.CharField(max_length=200)
    alternative_text = models.TextField()
    url = models.ImageField()
    order = models.IntegerField()
    
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    is_active = models.BooleanField()
    
class SeasonalEvent(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=200)
    