from django.db import models
from django.conf import settings

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
class Genre(models.Model):
    name=models.CharField(unique=True)
class Book(models.Model):
    title=models.CharField(max_length=100)
    isbn=models.CharField(max_length=20)
    author=models.ForeignKey('Author', on_delete=models.RESTRICT,null=True)
    genre=models.ManyToManyField(Genre,null=True)
    summary=models.CharField(max_length=1000)
    number_of_times_checked_out=models.IntegerField()
    date_checked_out=models.DateTimeField(auto_now_add=True,blank=True)
class Language(models.Model):
    name=models.CharField(unique=True)
class Book_Instance(models.Model):
    book=models.ForeignKey('Book',on_delete=models.RESTRICT,null=True)
    status=models.CharField(max_length=100)
    due_back=models.DateTimeField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    language=models.ForeignKey('Language',on_delete=models.RESTRICT,null=True)