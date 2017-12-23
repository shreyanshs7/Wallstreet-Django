from __future__ import unicode_literals

from django.db import models

# Create your models here.
class portfolio(models.Model):
	share_id = models.CharField(max_length=120,blank=True,null=True)
	user_id = models.CharField(max_length=120,blank=True,null=True)
	quantity = models.IntegerField(default=0)
	

class UserHolding(models.Model):
	user_id = models.CharField(max_length=120,blank=True,null=True)
	time = models.TimeField(auto_now=True)
	holdings = models.FloatField(default=10000.00)

class CurrentUserHolding(models.Model):
	user_id = models.CharField(max_length=120,blank=True,null=True)
	current_holdings = models.FloatField(default=10000.00)

class Transaction(models.Model):
	SELL = 'SL'
	BUY = 'BY'
	TRANSACTION_TYPE = (
		(SELL,'Sell'),
		(BUY,'Buy'),
		)
	share = models.CharField(max_length=120)
	transaction = models.CharField(max_length=20,choices=TRANSACTION_TYPE)