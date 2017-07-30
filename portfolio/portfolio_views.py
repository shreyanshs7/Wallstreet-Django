from django.shortcuts import render
from sellbuy.models import *
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def sellbuy(request):

	if request.method == "POST":

		share_choice = request.POST.get('dropdown')
		quantity = int(request.POST.get('quantity'))
		user = request.user
		print(request.POST)
		if quantity>int(0):

			if request.POST.get("button") == "BUY":
			

				try:
					buy_obj = portfolio.objects.get(share_id=share_choice,user_id=user)
					buy_share_quantity = buy_obj.quantity

					setattr(buy_obj , 'quantity' , buy_share_quantity+quantity)
					buy_obj.save()


				except portfolio.DoesNotExist:
				
					new_obj = portfolio.objects.create(share_id=share_choice,user_id=user,quantity=quantity)
				

						
				return HttpResponse("Share Bought")

			if request.POST.get("button") == "SELL":
				try:
					sell_obj = portfolio.objects.get(share_id=share_choice,user_id=user)
					sell_share_quantity = sell_obj.quantity
			
					if sell_share_quantity>=quantity:
					
						setattr(sell_obj, 'quantity' , sell_share_quantity-quantity)
						sell_obj.save()

						return HttpResponse("Shares Sold")

					else:
						return HttpResponse("You don't have enough shares !")	
				
				except portfolio.DoesNotExist:
					return HttpResponse("You have not bought these shares !")		
		
		else:
			return HttpResponse("You cannot fool me :)")	

					
			
				

		


	