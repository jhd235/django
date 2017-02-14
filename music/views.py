from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, World")
	return HttpResponse("This is from PyCharm")
# Create your views here.
