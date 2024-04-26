from django.http import HttpResponse
import requests
from django.shortcuts import render
from ipware import get_client_ip


def index(request):
  #return HttpResponse("Hello Word")
  return render(request, 'index.html')
