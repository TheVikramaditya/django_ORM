from django.contrib import admin
from . models import *
# Register your models here.



#providing additional features to model by creating classes
class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug':('name',)}#when creating name , slug field automatically populated
    # the above is commented as i am using save function to override or creating slug
    search_fields = ['name']
    list_display = ['id','name','is_active','parent']
    #  Allow editing of fields directly in the list
    list_editable = ('name',)
    # list_display_links = ('id',)




class ProductAdmin(admin.ModelAdmin):
    # add filters to the right side
    list_filter = ('stock_status',)
    
admin.site.register(Category,CategoryAdmin)#model, features
admin.site.register(Product,ProductAdmin)