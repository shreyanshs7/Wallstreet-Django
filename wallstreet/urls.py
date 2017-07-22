"""wallstreet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from register import views
from sellbuy import sellbuy_views
from api import api_views
from django.contrib.auth import views as auth_views
from portfolio import portfolio_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.registerview.as_view() , name='register'),
    url(r'^login/', auth_views.login , name='login'),
    url(r'^login_check/', views.login_check , name='login_check'),
    url(r'^api/users/', api_views.users_api , name='users_api'),
    url(r'^api/shareprice/', api_views.shareprice_api , name='share_api'),
    url(r'^shareprice/', sellbuy_views.share_price , name='share_price'),
    url(r'^currentprice/', sellbuy_views.current_price , name='current_price'),
    url(r'^sharegraph/(?P<name>\w+)/', portfolio_views.sharegraph , name='share_graph'),
    




]
