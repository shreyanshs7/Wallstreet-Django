from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse , JsonResponse
from .models import * 
from django.contrib.auth.decorators import login_required
from portfolio.models import *
from plotly.offline import plot
from plotly.graph_objs import Bar , Scatter
import datetime
from django.core import serializers
# Create your views here.

@login_required
def share_price(request):
	user = request.user
	share_obj = Share.objects.order_by("name")
	
	

	return render(request,"sellbuy/transaction.html",{"share_obj" :share_obj })

@login_required
def current_price(request):
	share_obj = Share.objects.order_by("name")
	
	portfolio_obj = portfolio.objects.filter(user_id=request.user)

	#left part for method for changing current price
	


	data=""
	share_worth = float(0)
	for obj in share_obj:
		data+="<tr><td class='center'>"+ str(obj.current_price) +"</td></tr>"
		share_worth += float(obj.current_price)

	total_quantity=int(0)	
	for obj in portfolio_obj:
		total_quantity += int(obj.quantity)

	holdings = share_worth * total_quantity	
	
	#below line of code will be shifted in method for changing current price
	#user_holding_obj = UserHolding.objects.create(user_id=request.user , time=datetime.datetime.now().time(), holdings=holdings)	
		
	return HttpResponse(data)




@login_required
def currentholding(request):
	user = request.user
	current_user_holding_obj = CurrentUserHolding.objects.get(user_id=user)
	current_holding = current_user_holding_obj.current_holdings

	return HttpResponse(current_holding)


@login_required
def current_quantity(request):
	user = request.user
	portfolio_obj = portfolio.objects.order_by("share_id").filter(user_id=user).distinct()


	data=""
	for obj in portfolio_obj:
		data+="<tr><td class='center'>"+str(obj.quantity)+"</td></tr>"

	return HttpResponse(data)	



@login_required
def sharegraph(request,name):
	share_obj = Share.objects.get(name=name)
	share_price_obj = SharePrice.objects.filter(share=share_obj)
	x=[]
	y=[]

	for obj in share_price_obj:
		x.append(obj.time)
		y.append(obj.price)
	
	


	return HttpResponse(plot([Scatter(x=x, y=y)],auto_open=False,output_type='div'))	






	
	




