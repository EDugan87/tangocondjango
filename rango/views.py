from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello there partner!")

def about(request):
    return HttpResponse('Welcome to the about section! <br /><a href="/rango/">Home</a><br />')