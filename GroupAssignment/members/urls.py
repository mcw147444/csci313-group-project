from django.urls import path, include
from . import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('account/<int:pk>', views.MemberDetailView.as_view(), name='member-detail'),
        path('loaned/',views.LoanedBooksView,name="loaned"),
]