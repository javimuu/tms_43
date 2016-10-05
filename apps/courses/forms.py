from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(
                attrs={'rows': 10, 'class': 'form-control', 'style': 'resize:vertical;',
                    'placeholder': 'Write some thing...'}),
            'status': forms.Select(
                            attrs={'class': 'form-control selector', 'title': 'Status'})
        }

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)


