from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse , JsonResponse
from .models import * 
from django.contrib.auth.decorators import login_required
from portfolio.models import *
from plotly.offline import plot
from plotly.graph_objs import Bar

# Create your views here.

@login_required
def share_price(request):
	share_obj = Share.objects.order_by("name").distinct()
		

	return render(request,"transaction.html",{"share_obj" :share_obj })

@login_required
def current_price(request):
	share_obj = Share.objects.order_by("name").distinct()	

	data=""
	for obj in share_obj:
		data+="<tr><td>"+ str(obj.current_price) +"</td></tr>"

	return HttpResponse(data)			

def current_quantity(request):
	portfolio_obj = portfolio.objects.order_by("share_id").distinct()

	data=""
	for obj in portfolio_obj:
		data+="<tr><td>"+str(obj.quantity)+"</td></tr>"

	return HttpResponse(data)	

def sharegraph(request,name):
	pass 
	
		

	return HttpResponse(plot([Bar(x=x, y=y)],auto_open=False,output_type='div'))	






	
	




