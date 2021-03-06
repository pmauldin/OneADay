from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.db import connection

from OneADay.models import Subscriber, Interest


def interests(request):
	if not request.user.is_authenticated() or request.user.username == 'admin':
		logout(request)
		return render(request, 'OneADay/auth/login.html', {'error': ""})

	subscriber = Subscriber.objects.get(user_id=request.user.id)
	keywords = subscriber.keywords.all()
	return render(request, 'OneADay/internal/interests.html', {'interests': keywords})


def add_interest(request):
	if not request.user.is_authenticated() or request.method != 'POST':
		return redirect('web:interests')

	subscriber = Subscriber.objects.get(user_id=request.user.id)
	interest, created = Interest.objects.get_or_create(keyword=request.POST['keyword'])

	subscriber.keywords.add(interest)
	subscriber.save()

	return HttpResponse("Added")


def remove_interest(request):
	if not request.user.is_authenticated() or request.method != 'POST':
		return redirect('web:interests')

	subscriber = Subscriber.objects.get(user_id=request.user.id)
	interest = Interest.objects.get(keyword=request.POST['keyword'])

	subscriber.keywords.remove(interest)
	subscriber.save()

	cursor = connection.cursor()
	cursor.execute("delete from Interest where Keyword not in (select interest_id from Subscriber_keywords)")

	return HttpResponse("Removed")


def trending(request):
	if not request.user.is_authenticated() or request.user.username == 'admin':
		logout(request)
		return render(request, 'OneADay/auth/login.html', {'error': ""})

	return render(request, 'OneADay/internal/trending.html')
