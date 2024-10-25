from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.

class AuthorInline(admin.TabularInline):
    model = Book
    fields = ['title']


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [AuthorInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Register BookInstance
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

    list_display = ('book', 'status', 'due_back', 'id')


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register Genre
admin.site.register(Genre)
# Register Language
admin.site.register(Language)


