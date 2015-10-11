from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse

from OneADay.models import Subscriber, Interest


def index(request):
	if not request.user.is_authenticated() or request.user.username == 'admin':
		logout(request)
		return render(request, 'OneADay/auth/login.html', {'error': ""})

	subscriber = Subscriber.objects.get(user_id=request.user.id)
	interests = subscriber.keywords.all()
	return render(request, 'OneADay/index.html', {'interests': interests})

def add_interest(request):
	if not request.user.is_authenticated() or request.method != 'POST':
		return redirect('web:index')

	subscriber = Subscriber.objects.get(user_id=request.user.id)
	interest, created = Interest.objects.get_or_create(keyword=request.POST['keyword'])

	subscriber.keywords.add(interest)
	subscriber.save()

	return HttpResponse("Added")


def remove_interest(request):
	if not request.user.is_authenticated() or request.method != 'POST':
		return redirect('web:index')

	subscriber = Subscriber.objects.get(user_id=request.user.id)
	interest = Interest.objects.get(keyword=request.POST['keyword'])

	subscriber.keywords.remove(interest)
	subscriber.save()

	return HttpResponse("Removed")