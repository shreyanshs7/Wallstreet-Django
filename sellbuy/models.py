from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Share(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=120,blank=True,null=True)
	current_price = models.FloatField(default=1000.0000)

	def __str__(self):
		return str(self.name)

class SharePrice(models.Model):
	share = models.ForeignKey('Share')
	price = models.FloatField(default=1000.00)
	time = 	models.TimeField(auto_now=True)

	

	
