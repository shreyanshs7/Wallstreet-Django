from django.contrib import admin
from .models import *
# Register your models here.


class portfolioAdmin(admin.ModelAdmin):
	list_display = ['user_id','share_id','quantity']
admin.site.register(portfolio,portfolioAdmin)	