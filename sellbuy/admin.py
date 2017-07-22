from django.contrib import admin
from .models import *
# Register your models here.

class ShareAdmin(admin.ModelAdmin):
	list_display = ['__str__','id','name','price']
admin.site.register(Share,ShareAdmin)	

class SharePriceAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'name','current_price','time']
admin.site.register(SharePrice,SharePriceAdmin)	