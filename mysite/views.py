from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse("<h1 style = \"color: white; background-color: blue;\"><center>Hello world!</center></h1>")
	