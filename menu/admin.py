from django.contrib import admin
from .models import Menu, formLogin


#Register your models here.
class MenuAdmin(admin.ModelAdmin):
      list_display = ("nama_product", "harga",)
  
admin.site.register(Menu, MenuAdmin)
admin.site.register(formLogin)