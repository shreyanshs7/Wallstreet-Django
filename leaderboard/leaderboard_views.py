from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from portfolio.models import *
from django.core import serializers
import json
# Create your views here.

def leaderboard(request):
	portfolio_obj = CurrentUserHolding.objects.order_by("current_holdings").reverse()
	
	return render(request,'leaderboard/leaderboard.html',{'portfolio_obj' : portfolio_obj })
		

def leaderboard_update(request):
	portfolio_obj = CurrentUserHolding.objects.order_by("current_holdings").reverse()

	html=""
	for obj in portfolio_obj:
		html+="<tr><td class='center red-text text-darken-4'><b>"+str(obj.user_id)+"</b></td><td class='center'>"+str(obj.current_holdings)+"</td></tr>"
		

		
	return HttpResponse(html)	