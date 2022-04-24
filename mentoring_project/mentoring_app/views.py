from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from mentoring_app.models import Mentor
from django_filters.views import FilterView
from mentoring_app.filters import MentorFilter

def index(request):
    return render(request, 'index.html')

def guidelines(request):
    return render(request, "guidelines.html")

class SubmissionFormView(TemplateView):
    template_path='ask_for_help.html'

    def get(self, request):
        return render(request, self.template_path)

class MentorListView(FilterView):
    template_name="mentors.html"
    paginate_by=10
    filterset_class = MentorFilter
    queryset = Mentor.objects.all()