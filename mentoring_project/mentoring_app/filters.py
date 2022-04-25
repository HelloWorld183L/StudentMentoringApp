from django_filters import FilterSet, CharFilter, NumberFilter
from mentoring_app.models import Mentor

class MentorFilter(FilterSet):
    class Meta:
        model = Mentor
        fields = {
            'current_year': ['gt'],
            'course': ['exact']
        }