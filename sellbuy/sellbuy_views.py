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
		temp_share_buy = Transaction.objects.filter(share=share,transaction='BY').exists()
		temp_share_sell = Transaction.objects.filter(share=share,transaction='SL').exists()

		if temp_share_sell or temp_share_buy:
			temp_share_buy_count = Transaction.objects.filter(share=share,transaction='BY').count()
			temp_share_sell_count = Transaction.objects.filter(share=share,transaction='SL').count()

			if temp_share_buy_count > temp_share_sell_count:
				share_price = (share.current_price) * (1 + random.uniform(0.1,0.5))
				
				if share_price>float(25000):
					share_price = (share_price) * (random.uniform(0.1,0.3))
				
				new_share = SharePrice.objects.create(share=share,price=share_price)
				new_share.save()
				
				setattr(share,'current_price',share_price)
				share.save()

			else:
				share_price = (share.current_price) * (random.uniform(0.1,0.5))
				
				if share_price < float(200):
					share_price = (share_price) * (1 + random.uniform(0.1,0.3))

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






	
	




