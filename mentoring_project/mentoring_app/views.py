from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from mentoring_app.models import Mentor

BASE_TEMPLATE_PATH = 'templates/'

def index(request):
    return render(request, 'index.html')

def guidelines(request):
    return render(request, "guidelines.html")

class SubmissionFormView(TemplateView):
    template_path=BASE_TEMPLATE_PATH+'ask_for_help.html'

    def get(self, request):
        return render(request, self.template_path)

class MentorListView(ListView):
    model = Mentor
    context_object_name = 'mentor_list'
    template_path=BASE_TEMPLATE_PATH+'mentors.html'
    paginate_by = 10

    def get(self, request):
        mentors = Mentor.objects.all()

        args = {'mentors': mentors}
        return render(request, self.template_path, mentors)
