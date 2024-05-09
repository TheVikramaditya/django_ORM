from django.db import models
import uuid
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    pid = models.CharField(max_length=200,null=False,blank=False)
    slug = models.SlugField()#URL friendly string , we can use "unique" here and in name
    description = models.TextField(null=True)
    is_digital = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)#date time will not update , but only created for first time
    upted_at = models.DateTimeField(auto_now=True,editable=False)
    is_active = models.BooleanField(default=True)
    
    IN_STOCK = "IS"
    OUT_OF_STOCK = "OOS"
    BACKORDERED = "BO"
    
    STOCK_STATUS = {
        IN_STOCK : "In Stock",
        OUT_OF_STOCK: "Out of stock",
        BACKORDERED: "Back Ordered"
    }
    status = models.CharField(max_length=3,choices=STOCK_STATUS,default=IN_STOCK)
    
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
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField()
    
class SeasonalEvent(models.Model):
    id = models.BigAutoField(primary_key=True)#BigAutoField = auto increment field
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=200)
    