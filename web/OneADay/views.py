from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from datetime import datetime

from .models import Subscriber


def index(request):
	return render(request, 'OneADay/index.html', {'subscribers': Subscriber.objects.all()})


def select(request):
	person = Subscriber.objects.get(firstname=request.POST['person'])
	interests = person.keywords.all()

	return render(request, 'OneADay/interests.html', {'interests': interests})


def login(request):
	if request.method == 'GET':
		return render(request, 'OneADay/auth/login.html')
	elif request.method != 'POST':
		raise Http404

	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)

	if user is not None:
		return render(request, 'OneADay/interests.html')



def register(request):
	if request.method == 'GET':
		return render(request, 'OneADay/auth/register.html')
	elif request.method != 'POST':
		raise Http404

	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']

	user = User.objects.create_user(username, email, password)

	Subscriber.objects.create(user=user, joindate=datetime.now())

	return render(request, 'OneADay/auth/registerSuccess.html', {'name': username})
