from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Share(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=120,blank=True,null=True)
	current_price = models.DecimalField(max_digits=7,decimal_places=2,default=1000.0000)

	def __str__(self):
		return str(self.name)

class SharePrice(models.Model):
	share = models.ForeignKey('Share')
	price = models.DecimalField(max_digits=20,decimal_places=2,default=1000.00)
	time = 	models.TimeField()

	def __str__(self):
		return str(self.share.name)