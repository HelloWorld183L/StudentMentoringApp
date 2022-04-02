from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.guidelines, name='guidelines'),
    path('', views.mentor_list, name='mentor_list'),
    path('', views.ask_for_help, name='ask_for_help')
]
