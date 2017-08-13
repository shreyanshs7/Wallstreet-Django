from django.shortcuts import render
from .models import UserDetails
from .forms import RegistrationForm
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View 
from django.http import HttpResponse , HttpResponseRedirect , JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from portfolio.models import *
import datetime
from sellbuy.models import *

# Create your views here.
def index(request):
	return render(request,'index.html')


@csrf_protect
def login_check(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/shareprice")
	else:
		return HttpResponseRedirect('/login')
			



class registerview(View):
	form_class = RegistrationForm
	template_name = 'registration/registration_form.html'

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})


	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			email = form.cleaned_data['email']
			branch = form.cleaned_data['branch']
			college = form.cleaned_data['college']
			contact = form.cleaned_data['contact']

			user.set_password(password)
			user.save()

			userdetail = UserDetails.objects.create(name=username,
				college=college,
				branch=branch,
				email=email,
				contact=contact)
			userdetail.save()

			user_holding = UserHolding.objects.create(
				user_id=username,
				time=datetime.datetime.now().time() 
				)
			user_holding.save()

			current_holding = CurrentUserHolding.objects.create(
				user_id=username)
			current_holding.save()

			share_obj = Share.objects.all()

			for obj in share_obj:
				portfolio_obj = portfolio.objects.create(
					share_id=obj.name,
					user_id=username,
					quantity=0
					)
				portfolio_obj.save()
				



			return HttpResponseRedirect("/login")


		return render(request,self.template_name,{'form':form})	









