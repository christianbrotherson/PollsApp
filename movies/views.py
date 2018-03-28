from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("I've also created a movies index for you since you seem to be moving so quickly!")