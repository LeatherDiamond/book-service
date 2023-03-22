from django.contrib import admin
from product_card.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    """Creating Admin interface"""
    list_display = ('name', 'book_author', 'publishing_year', 'pages', 'binding', \
    'format', 'isbn', 'weight', 'age_restriction', 'date_of_addition', 'modification_date')


    def book_author(self, obj):
        """Printing models with M2M in Admin interface"""
        return ", ".join([p.name + " " + p.surname for p in obj.author.all()])

admin.site.register(Book, BookAdmin)