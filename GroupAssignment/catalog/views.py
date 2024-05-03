from django.shortcuts import render
from django.views import generic
from .models import Book

# Create your views here.
def home(request):
    context={}
    return render(request, 'index.html',context=context)
class BookListView(generic.ListView):
    model = Book