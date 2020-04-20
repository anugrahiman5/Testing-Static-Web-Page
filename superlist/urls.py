from django.conf.urls import url
from django.contrib import admin
from lists import views
from django.http import HttpResponse

def index(request):
	return HttpResponse("<title>Anugrah Iman</title><h1>Anugrah Iman Setyo Utomo</h1>")

urlpatterns = [
	#url(r'^$', 'home', name='home'),
	#url(r'^$', views.home_page, name='home'),
	url(r'^admin/', admin.site.urls),
	url(r'^$', index),
]
