from django_filters import FilterSet, CharFilter, NumberFilter
from mentoring_app.models import Mentor

class MentorFilter(FilterSet):
    course = CharFilter(lookup_expr='icontains')
    current_year = NumberFilter(field_name='current_year', lookup_expr='current_year')
    current_year__gt = NumberFilter(field_name='current_year', lookup_expr='current_year__gt')    
    current_year__lt = NumberFilter(field_name='current_year', lookup_expr='current_year__lt')