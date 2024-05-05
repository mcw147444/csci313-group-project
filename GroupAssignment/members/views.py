from django.shortcuts import render
from catalog.models import Book_Instance

from .models import Member
from django.contrib.auth.models import User

from django.views import generic
# Create your views here.
def account(request):
    context={}
    return render(request, 'account.html', context)
def LoanedBooksView(request):
    context={}
    instance_list=Book_Instance.objects.filter(borrower=request.user)
    instance_dictionary={'instance':instance_list}
    return render(request,'account/loaned_books.html',context=instance_dictionary)

class MemberDetailView(generic.DetailView):
    model = Member