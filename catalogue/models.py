from django.db import models
import uuid
# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name="category name",help_text="enter a category")
    slug = models.SlugField(unique=True,null=True,blank=True)
    is_active = models.BooleanField()
    
    #self referencing foreign key , when a model needs to establish a relationship with itself
    #i.e = Clothes > Shoes > Boot,  here Shoes parent will be Clothes , and Boot's will be Shoes
    parent = models.ForeignKey('self',on_delete=models.PROTECT,null=True,blank=True)
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
    
    
    #overrididng the default save model
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)
        
    
    
    def __str__(self):
        return self.name
    
class SeasonalEvent(models.Model):
    id = models.BigAutoField(primary_key=True)#BigAutoField = auto increment field
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=200)




class Attribute(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    
    
    
class AttributeValue(models.Model):
    attribute_value = models.CharField(max_length=200)
    attribute = models.ForeignKey(Attribute,on_delete=models.CASCADE)
    

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self',on_delete=models.CASCADE)





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
    stock_status = models.CharField(max_length=3,choices=STOCK_STATUS,default=IN_STOCK)
    
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    seasonal_event = models.ForeignKey(SeasonalEvent,on_delete=models.SET_NULL,null=True)#some products are specially for some festivals
    
    #Django is going to build a new table for many to many relationship , called linked table
    product_type = models.ManyToManyField(ProductType,related_name="product_type")
    
    def __str__(self):
        return self.name
    


class ProductLine(models.Model):
    price = models.DecimalField(max_digits=8,decimal_places=2)
    sku = models.UUIDField(default=uuid.uuid4)
    stock_qty = models.IntegerField()
    order = models.IntegerField()
    weight = models.FloatField()
    product = models.ForeignKey(Product,on_delete=models.PROTECT,default=None)
    attribute_value = models.ManyToManyField(AttributeValue,related_name="product_lines")

class ProductImage(models.Model):
    name = models.CharField(max_length=200)
    alternative_text = models.TextField()
    url = models.ImageField()
    order = models.IntegerField()
    #ON_DELETE are of following types
    # 1 - CASCADE = when a referenced row in the parent table is deleted, all corresponding rows in the child table will also be deleted automatically.
    # 2 - PROTECT =  if there are any child rows referencing a parent row, the deletion of the parent row is prevented.
    # 3 - SET_NULL = this option sets the foreign key in the child table to NULL
    # 5 - SET_DEFAULT = this option sets the foreign key in the child table to a default value specified by the database schema.
    # 6 - SET() = specify a custom value or expression to set the foreign key in the child table when a referenced row in the parent table is deleted.
    #7  - DO_NOTHING = no action is taken on the corresponding rows in the child table.could potentially lead to referential integrity issues if not handled properly.
    product_line = models.ForeignKey(ProductLine,on_delete=models.CASCADE,default=None)
    
    
class StockControl(models.Model):
    stock_qty = models.IntegerField()
    name = models.CharField(max_length=100)
    stock_product = models.OneToOneField(Product,on_delete=models.CASCADE)
     