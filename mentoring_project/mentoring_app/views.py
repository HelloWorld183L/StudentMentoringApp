from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def mentor_list(request):
    return render(request, 'mentor_list.html')

def guidelines(request):
    return render(request, "guidelines.html")

def ask_for_help(request):
    return HttpResponse(request, "ask_for_help.html")
