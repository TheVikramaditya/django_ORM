from django.contrib import admin
from . models import *
# Register your models here.



#providing additional features to model by creating classes
class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug':('name',)}#when creating name , slug field automatically populated
    # the above is commented as i am using save function to override or creating slug
    pass
    
    
admin.site.register(Category,CategoryAdmin)#model, features
admin.site.register(Product)