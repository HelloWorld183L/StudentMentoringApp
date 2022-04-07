from django import forms
from mentoring_app.models import Student

class SubmissionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control'
        }
    ))
    course = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control'
        }
    ))
    

    class Meta:
        model = Student
        
