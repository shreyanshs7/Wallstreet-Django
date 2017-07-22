from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserDetails(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=120,blank=True,null=True)
	college=models.CharField(max_length=120,blank=True,null=True)
	branch=models.CharField(max_length=120,blank=True,null=True)
	email=models.CharField(max_length=120,blank=True,null=True)
	contact=models.DecimalField(max_digits=11,decimal_places=0,blank=True,null=True)

	def __str__(self):
		return self.name