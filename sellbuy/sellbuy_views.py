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
import random



@login_required
def share_price(request):
	user = request.user
	share_obj = Share.objects.order_by("name")
	
	

	return render(request,"sellbuy/transaction.html",{"share_obj" :share_obj })

@login_required
def current_price(request):
	share_obj = Share.objects.order_by("name")
	shares = Share.objects.all() 
	
	for share in shares:
			share_price = (share.current_price) * (random.uniform(0.8,1.3))
			
			share_price = round(share_price,2)

			new_share = SharePrice.objects.create(share=share,price=share_price)
			new_share.save()

			setattr(share,'current_price',share_price)
			share.save()
	
	portfolio_obj = portfolio.objects.filter(user_id=request.user)
	

	total_share_value = float(0)
	total_quantity = float(0)

	for obj in portfolio_obj:

		temp_share = Share.objects.get(name=obj.share_id)
		total_share_value += temp_share.current_price
		total_quantity += obj.quantity

	holdings = float(total_share_value) * float(total_quantity)	

	holdings = round(holdings,2)

	user_holding_obj = UserHolding.objects.create(user_id=str(request.user),holdings=holdings)
	user_holding_obj.save()	


	data=""
	
	for obj in share_obj:
		data+="<tr><td class='center'>"+ str(obj.current_price) +"</td></tr>"
			

	
		
		
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






	
	




