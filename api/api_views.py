from django.shortcuts import render
from register.models import *
from sellbuy.models import *
from django.core import serializers
from django.http import JsonResponse
import json

# Create your views here.

def share_api(request):
	share_obj = Share.objects.all()
	share_json = serializers.serialize("json",share_obj)
	share_data = json.loads(share_json)
	share_list = []
	
	for data in share_data:
		share_list.append(data['fields'])

	share_api = json.dumps(share_list)	


	return JsonResponse(share_api,safe=False)

def users_api(request):
	users_obj = UserDetails.objects.all()
	users_json = serializers.serialize("json",users_obj)
	users_data = json.loads(users_json)
	users_list = []
	
	for data in users_data:
		users_list.append(data['fields'])

	users_api = json.dumps(users_list)	

	return JsonResponse(users_api,safe=False)	


	