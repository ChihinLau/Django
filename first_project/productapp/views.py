from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse("<h1>product home</h1>")

def about(reuqest):
	return HttpResponse("<h1>product about</h1>")