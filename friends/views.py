from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Here is a friends index")

# Create your views here.
