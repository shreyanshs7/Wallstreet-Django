from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse , JsonResponse
from .models import * 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def share_price(request):
	share_obj = SharePrice.objects.filter()
	
	return render(request,"transaction.html",{"share_obj" :share_obj})

@login_required
def current_price(request):
	share_obj = SharePrice.objects.filter()

	#left part for changing current share price
	data=""
	for obj in share_obj:
		data+= "<tr><td class=\'center\'>"+str(obj.current_price)+"</td></tr>"

	return HttpResponse(data)		




