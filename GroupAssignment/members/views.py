from django.shortcuts import render

from .models import Member
from django.contrib.auth.models import User

from django.views import generic
# Create your views here.
def account(request):
    context={}
    return render(request, 'account.html', context)

class MemberDetailView(generic.DetailView):
    model = Member