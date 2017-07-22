from django.contrib import admin
from .models import UserDetails
# Register your models here.
class UserDetailsAdmin(admin.ModelAdmin):
	list_display = ['__str__' ,'id','name','college','branch' , 'email','contact']
	
admin.site.register(UserDetails,UserDetailsAdmin)