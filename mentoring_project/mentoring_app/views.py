from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'templates/index.html')

def mentor_list(request):
    return render(request, 'templates/mentor_list.html')

def guidelines(request):
    return render(request, "templates/guidelines.html")

def ask_for_help(request):
    return HttpResponse(request, "templates/ask_for_help.html")
