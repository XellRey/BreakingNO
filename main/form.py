from django.forms import ModelForm, TextInput, Textarea
from .models import Statement


class CreateStatement(ModelForm):
    class Meta:
        model = Statement
        fields = ['name', 'car_num', 'description']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name'}),
            'car_num': TextInput(attrs={'placeholder': 'Registration Number'}),
            'description': Textarea(attrs={'placeholder': 'Description'}),
        }

        labels = {
            'name': '',
            'car_num': '',
            'description': ''
        }