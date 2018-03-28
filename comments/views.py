from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("And now you're at the comments index! You're really getting around!")