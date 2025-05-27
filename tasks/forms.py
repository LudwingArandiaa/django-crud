from django import forms
from .models import Task

# Create your forms here
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'write a title'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'write a description'}),
            '' : forms.CheckboxInput(attrs={'class' : 'form-check-input m-auto'}),
        }
