from django.contrib import admin
from .models import *
# Register your models here.

class ShareAdmin(admin.ModelAdmin):
	list_display = ['__str__','id','name','current_price']
admin.site.register(Share,ShareAdmin)	

class SharePriceAdmin(admin.ModelAdmin):
	list_display = ['share','price','time']
admin.site.register(SharePrice,SharePriceAdmin)	