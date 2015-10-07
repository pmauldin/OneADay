from django.shortcuts import get_object_or_404, render, redirect
from .models import Subscriber


def index(request):
	return render(request, 'OneADay/index.html', {'subscribers': Subscriber.objects.all()})

def select(request):
	person = Subscriber.objects.get(firstname=request.POST['person'])
	interests = person.keywords.all()

	return render(request, 'OneADay/interests.html', {'interests': interests})
