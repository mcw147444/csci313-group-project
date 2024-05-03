from django.contrib import admin
from catalog.models import Book,Author,Book_Instance,Genre,Language

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Book_Instance)
admin.site.register(Genre)
admin.site.register(Language)