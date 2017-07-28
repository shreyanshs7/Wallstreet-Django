from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse , JsonResponse
from .models import * 
from django.contrib.auth.decorators import login_required

from plotly.offline import plot
from plotly.graph_objs import Bar

# Create your views here.

@login_required
def share_price(request):
	share_obj = Share.objects.values("name").distinct()
	

	return render(request,"transaction.html",{"share_obj" :share_obj })

@login_required
def current_price(request):
	share_obj = Share.objects.all()

	#left part for changing current share price
	data=""
	for obj in share_obj:
		data+= "<tr><td class=\'center\'>"+str(obj.current_price)+"</td></tr>"

	return HttpResponse(data)		

def sharegraph(request,name):
	shareprice_obj = SharePrice.objects.filter(share__name=name)

	x=[]
	y=[]

	for obj in shareprice_obj:
		x.append(obj.time)
		y.append(obj.price)
	
		

	return HttpResponse(plot([Bar(x=x, y=y)],auto_open=False,output_type='div'))	





	
	




