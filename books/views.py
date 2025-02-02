from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Book
from django.db.models import Q

def home(request):
    return render(request, 'books/home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/books.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        published_date = request.POST.get('published_date')

        if Book.objects.filter(isbn=isbn).exists():
            return render(request, 'books/add_book.html', {'error': 'A book with this ISBN already exists.'})

        Book.objects.create(title=title, author=author, isbn=isbn, published_date=published_date)
        return redirect('books')

    return render(request, 'books/add_book.html')

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('books')

def search_books(request):
    query = request.GET.get('query', '')
    results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'books/search.html', {'results': results, 'query': query})




