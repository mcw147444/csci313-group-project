from datetime import date
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
import uuid

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Genre(models.Model):
    name=models.CharField(unique=True, max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry, etc.)")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            ),
        ]

class Book(models.Model):
    title=models.CharField(max_length=200)
    isbn=models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    author=models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    number_of_times_checked_out=models.IntegerField(editable=False)
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'
    
    def __str__(self):
        return self.title

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Enter the langauge of the book')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('language_detail', args=[str(self.id)])
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='language_name_case_insensitive_unique',
                violation_error_message = "Language already exists (case insensitive match)"
            ),
        ]

class Book_Instance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book=models.ForeignKey('Book',on_delete=models.RESTRICT,null=True)
    
    STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    
    date_checked_out=models.DateTimeField(auto_now_add=True, blank=True)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey('Language', on_delete=models.RESTRICT, null=True)
    
    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)
        
    def __str__(self):
        return f'{self.id} ({self.book.title})'
    
    def is_overdue(self):
        return bool(self.due_back and date.today() > self.due_back)