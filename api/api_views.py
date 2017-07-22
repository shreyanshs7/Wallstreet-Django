from django.shortcuts import render
from register.models import *
from sellbuy.models import *
from django.core import serializers
from django.http import JsonResponse
# Create your views here.

def shareprice_api(request):
	share_data = SharePrice.objects.all()
	share_json = serializers.serialize("json",share_data)

	return JsonResponse(share_json,safe=False)

def users_api(request):
	users_obj = UserDetails.objects.all()
	users_json = serializers.serialize("json",users_obj)
	
	return JsonResponse(users_json,safe=False)	