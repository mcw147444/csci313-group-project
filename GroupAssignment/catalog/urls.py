from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name="books"),
    path('members/', include('members.urls')),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    
]