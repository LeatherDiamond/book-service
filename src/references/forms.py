from django import forms
from . import models

#Forms for references

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.BookAuthor
        fields = ['name', 'surname', 'description']