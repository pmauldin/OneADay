from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^web/', views.index, name='index'),
	url(r'^select/', views.select, name='select'),
	url(r'^$', views.register, name='register'),
	url(r'^login/', views.login, name='login')
]