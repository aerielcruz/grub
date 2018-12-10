from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	context = {
		"title": "Welcome to home",
	}
	return render(request, "index.html", context)