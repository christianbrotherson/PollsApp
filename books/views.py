from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("And now you are at the books index!!")