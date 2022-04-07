from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guidelines', views.guidelines, name='guidelines'),
    path('mentor_list', views.mentor_list, name='mentor_list'),
    path('ask_for_help', views.ask_for_help, name='ask_for_help')
]
