import django.forms
from django.forms import Select, CheckboxInput, ModelForm, DateInput
from .models import Task


class CreateNewTaskForm(ModelForm):
    class Meta:
        model = Task

        fields = '__all__'

        widgets = {
            'priority': Select(attrs={'class': 'form-control'}),
            'status': CheckboxInput(attrs={'class': 'form-check-input'}),
            'deadline': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_of_creation': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }



class UpdateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'priority': Select(attrs={'class': 'form-control'}),
            'status': CheckboxInput(attrs={'class': 'form-check-input'}),
            'deadline': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_of_creation': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
