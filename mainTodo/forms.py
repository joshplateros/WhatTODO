from django import forms
from .models import Task

class DateTimeInput(forms.DateTimeInput):
    input_type = 'time'

class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields=['description', 'due_date', 'due_date_time']
        widgets = {
            'due_date': DateInput(),
            'due_date_time': DateTimeInput(),
        }
