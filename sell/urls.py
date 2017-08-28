from django.conf.urls import url
from . import views

app_name = 'sell'

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^post$', views.postbook, name = 'postbook'),
	url(r'^postb$', views.postb, name = "postb"),
	url(r'^ajaxsend$',views.ajaxsend, name = "ajaxsend"),
	url(r'^search$', views.search, name = "search"),
	url(r'^searchm$', views.searchm, name = "searchm"),
	url(r'^searchx(?P<page>)$', views.searchx, name = "searchx"),
]