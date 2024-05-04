from django.shortcuts import render
from .models import Book,Book_Instance
from django.views import generic

# Create your views here.
def index(request):
    context={}
    return render(request, 'index.html',context=context)

def LoanedBooksView(request):
    context={}
    instance_list=Book_Instance.objects.filter(borrower=request.user)
    instance_dictionary={'instance':instance_list}
    return render(request,'catalog/loaned_books.html',context=instance_dictionary)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    
class BookDetailView(generic.DetailView):
    model = Book
