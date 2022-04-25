from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guidelines', views.guidelines, name='guidelines'),
    path('mentors/', views.MentorListView.as_view(), name='mentors'),
    path('ask_for_help', views.SubmissionFormView.as_view(), name='ask_for_help')
]
