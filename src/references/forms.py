from django import forms
from . import models
from product_card import models

#Forms for references

class AuthorForm(forms.ModelForm):
    related_books = forms.ModelMultipleChoiceField(
        queryset=models.Book.objects.none(),
        widget=forms.CheckboxSelectMultiple(attrs={"checked":""}),
        disabled=True,
        required=False
    )
    
    class Meta:
        model = models.BookAuthor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['related_books'].queryset = models.Book.objects.filter(author=self.instance)
            self.fields['related_books'].initial = self.instance.book_set.all()

    def save(self, commit=True):
        author = super().save(commit=False)
        if commit:
            author.save()
            self.save_m2m()
        return author