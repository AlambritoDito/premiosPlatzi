from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("De un porte muy exuberante")

# Create your views here.
