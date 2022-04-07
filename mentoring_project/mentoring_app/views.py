from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from mentoring_app.models import Mentor

# Create your views here.

def index(request):
    return render(request, 'index.html')

def guidelines(request):
    return render(request, "guidelines.html")

def ask_for_help(request):
    return HttpResponse(request, "ask_for_help.html")

class SubmissionFormView(TemplateView):
    template_path='templates/ask_for_help.html'

    def get(self, request):
        return render(request, self.template_path)

    def post(self, request):
        form = SubmissionForm(request.POST)

        return render(request, self.template_name)
