from django.shortcuts import render
from .models import Book
from django.views import generic

# Create your views here.
def index(request):
    context={}
    return render(request, 'index.html',context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    
class BookDetailView(generic.DetailView):
    model = Book
