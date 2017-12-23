from django.shortcuts import render
from sellbuy.models import *
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from plotly.offline import plot
from plotly.graph_objs import Bar , Scatter
import datetime


# Create your views here.
@login_required
def sellbuy(request):

	if request.method == "POST":

		share_choice = request.POST.get('dropdown')
		quantity = int(request.POST.get('quantity'))
		user = request.user.username
		
		user_holding_obj = CurrentUserHolding.objects.get(user_id=user)
		current_holding = user_holding_obj.current_holdings

		share_obj = Share.objects.get(name=share_choice)
		share_price = share_obj.current_price

		

		if quantity>int(0):

			if request.POST.get("button") == "BUY":
				
				if share_price*quantity <= current_holding:

					try:

						transaction_obj = Transaction.objects.create(share=share_choice,transaction='BY')
						transaction_obj.save()


						buy_obj = portfolio.objects.get(share_id=share_choice,user_id=user)
						buy_share_quantity = buy_obj.quantity

						setattr(buy_obj , 'quantity' , buy_share_quantity+quantity)
						buy_obj.save()

						cash_in_hand = current_holding-(share_price*quantity)

						setattr(user_holding_obj , 'current_holdings' , cash_in_hand)
						user_holding_obj.save()
						
						

					except portfolio.DoesNotExist:
				
						new_obj = portfolio.objects.create(share_id=share_choice,user_id=user,quantity=quantity)
						

						
					return HttpResponse("Share Bought")

				else:
					return HttpResponse("Current Holding is less only "+str(int(current_holding/share_price))+" share can be bought")


			if request.POST.get("button") == "SELL":
				try:
					sell_obj = portfolio.objects.get(share_id=share_choice,user_id=user)
					sell_share_quantity = sell_obj.quantity
			
					if sell_share_quantity>=quantity:

						transaction_obj = Transaction.objects.create(share=share_choice,transaction='SL')
						transaction_obj.save()
					
						setattr(sell_obj, 'quantity' , sell_share_quantity-quantity)
						sell_obj.save()

						cash_in_hand = current_holding+(share_price*quantity)

						setattr(user_holding_obj , 'current_holdings' , current_holding+share_price*quantity)
						user_holding_obj.save()

						




						return HttpResponse("Shares Sold")

					else:
						return HttpResponse("You don't have enough shares !")	
				
				except portfolio.DoesNotExist:
					return HttpResponse("You have not bought these shares !")		
		
		else:
			return HttpResponse("You cannot fool me :)")	


@login_required
def profit_loss_graph(request,name):
	
	obj = UserHolding.objects.filter(user_id=name)

	x=[]
	y=[]

	for o in obj:
		x.append(o.time)
		y.append(o.holdings)

	return HttpResponse(plot([Scatter(x=x, y=y)],auto_open=False,output_type='div'))	

			
				

		


	