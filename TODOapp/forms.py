from django import forms
from TODOapp.models import  Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=[
            'title','status','priority',
        ]
        
