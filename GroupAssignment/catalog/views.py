from django.shortcuts import render
from .models import Book

# Create your views here.
def home(request):
    context={}
    return render(request, 'index.html',context=context)
def catalog(request):
    book_list=Book.objects.all()
    book_dictionary={'book':book_list}
    return render(request,'catalog/catalog.html',context=book_dictionary)
