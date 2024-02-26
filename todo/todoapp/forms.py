from django import forms
from .models import *



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo']
        
        
        widgets = {
            'todo': forms.TextInput(attrs={'class':'form-control w-25 border border-3 rounded-2 border-black m-2'})
        }
        
        
        