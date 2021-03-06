from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from datetime import datetime

from OneADay.models import Subscriber


def login_user(request):
	if request.user.is_authenticated():
		return redirect('web:interests')

	if request.method == 'GET':
		return render(request, 'OneADay/auth/login.html', {'error': ""})
	elif request.method != 'POST':
		raise Http404

	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)

	if user is not None:
		login(request, user)
		return redirect('web:interests')

	return render(request, 'OneADay/auth/login.html', {'error': "Incorrect username or password"})


def logout_user(request):
	logout(request)
	return redirect('web:interests')


def register(request):
	if request.method == 'GET':
		return render(request, 'OneADay/auth/register.html', {'error': ""})
	elif request.method != 'POST':
		raise Http404

	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']

	if User.objects.filter(email=email).count() > 0:
		return render(request, 'OneADay/auth/register.html', {'error': "That email address is already in use."})

	if User.objects.filter(username=username).count() > 0:
		return render(request, 'OneADay/auth/register.html', {'error': "That username is already in use."})

	user = User.objects.create_user(username, email, password)

	Subscriber.objects.create(user=user, joindate=datetime.now())

	return render(request, 'OneADay/auth/registerSuccess.html', {'name': username})
