from django.shortcuts import render
from django.apps import apps
from django.http import HttpResponse
from plotly.offline import plot
from plotly.graph_objs import Bar

# Create your views here.
def sharegraph(request,name):

	model = apps.get_model('portfolio',name)

	x1=[]
	y1=[]

	for data in model.objects.all():

		x1=append(data.x)
		y1=append(data.y)

	return HttpResponse(plot([Bar(x=x1 , y=y1 )], auto_open=False , output_type='div'))	
