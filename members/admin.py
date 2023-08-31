from django.contrib import admin
from .models import Product
from .models import BlogPost


# admin.site.register(BlogPost)
# admin.site.register(Product)

class MemberAdmin(admin.ModelAdmin):
  list_display = ("title", "content", "pub_date", "author")
  

admin.site.register(BlogPost, MemberAdmin)

class MemberAdmin(admin.ModelAdmin):
  list_display = ("name", "price", "description",)
  
admin.site.register(Product, MemberAdmin)


