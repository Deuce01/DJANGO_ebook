from django.shortcuts import render, get_object_or_404
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'library/index.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})
