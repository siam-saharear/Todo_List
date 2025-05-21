from django import forms

from .models import *

from django.forms import ModelForm


class CategoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields = [
            "name",
            "description",
            "type",
        ]

class TaskForm(ModelForm):
    
    class Meta:
        model = Task
        fields = [
            
            "name",
            "descripiton",
            "type",
        ]
        # fields = "__all__"
        