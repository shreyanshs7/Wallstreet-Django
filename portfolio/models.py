from __future__ import unicode_literals

from django.db import models

# Create your models here.
class portfolio(models.Model):
	share_id = models.CharField(max_length=120,blank=True,null=True)
	user_id = models.CharField(max_length=120,blank=True,null=True)
	quantity = models.IntegerField(default=0)

	