from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from mentoring_app.models import Mentor

# Create your views here.

def index(request):
    return render(request, 'index.html')

def mentor_list(request):
    return render(request, 'mentor_list.html')

def guidelines(request):
    return render(request, "guidelines.html")

def ask_for_help(request):
    return render(request, 'ask_for_help.html')

class MentorListView(TemplateView):
    template_path = "templates/mentor_list.html"

    def get(self,request):
        mentors = Mentor.objects.all()
        
        args = {'mentors': mentors}
        return render(request, self.template_path, args)
