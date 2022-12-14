from .models import *
from django import forms

from django.forms import ModelForm


class UploadModelForm(forms.Form):
    file = forms.FileField()

    class Meta:
        model = UploadFileModel


# class UploadModelForm(forms.ModelForm):
#     class Meta:
#         model = UploadFileModel
#         fields = ('description', 'document', )



class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username', 'password', 'date_of_join')
        labels = {
            'first_name': '',
            'last_name': '',
            'username': '',
            'password': '',
            'date_of_join': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
            'date_of_join': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'date_of_join'}),
            'file_field': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'input file'}),
        }

