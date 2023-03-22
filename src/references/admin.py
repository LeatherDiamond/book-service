from django.contrib import admin

from .models import BookAuthor


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'related_books', 'description']

    def full_name(sel, obj):
        return f"{obj.name} {obj.surname}"

    def related_books(self, obj):
        return ', '.join([book.name for book in obj.book_set.all()])
    related_books.short_description = 'Related Books'


admin.site.register(BookAuthor, AuthorAdmin)