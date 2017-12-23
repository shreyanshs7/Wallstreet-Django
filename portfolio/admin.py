from django.contrib import admin
from .models import *
# Register your models here.


class portfolioAdmin(admin.ModelAdmin):
	list_display = ['user_id','share_id','quantity']
admin.site.register(portfolio,portfolioAdmin)

class UserHoldingAdmin(admin.ModelAdmin):
	list_display = ['user_id','time','holdings']
admin.site.register(UserHolding,UserHoldingAdmin)	

class CurrentUserHoldingAdmin(admin.ModelAdmin):
	list_display = ['user_id','current_holdings']
admin.site.register(CurrentUserHolding,CurrentUserHoldingAdmin)	

class TransactionAdmin(admin.ModelAdmin):
	list_display = ['share','transaction']
admin.site.register(Transaction,TransactionAdmin)	