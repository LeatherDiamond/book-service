from django import forms
from . import models


class DateInput(forms.DateInput):
    input_type = 'date'


class ProductCardForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['name', 'image', 'author', 'publishing_year', 'pages', 'binding',\
         'format', 'isbn', 'weight', 'age_restriction','date_of_addition', 'description'
         ]
        widgets = {'date_of_addition' : DateInput()}