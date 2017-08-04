from __future__ import unicode_literals

from django.db import models

# Create your models here.
class portfolio(models.Model):
	share_id = models.CharField(max_length=120,blank=True,null=True)
	user_id = models.CharField(max_length=120,blank=True,null=True)
	quantity = models.IntegerField(default=0)

class UserHolding(models.Model):
	user_id = models.CharField(max_length=120,blank=True,null=True)
	time = models.TimeField()
	holdings = models.DecimalField(max_digits=20,decimal_places=2,default=10000.00)

class CurrentUserHolding(models.Model):
	user_id = models.CharField(max_length=120,blank=True,null=True)
	current_holdings = models.DecimalField(max_digits=20,decimal_places=2,default=10000.00)
