from django.shortcuts import render

# Create your views here.
from books.models import Author, Book, Genre


def index(request):
    return render(request, 'base.html')


def detail_author_view(request, id):
    author = Author.objects.get(pk=id)
    return render(request, 'author_detail_view.html', {'author': author})

def detail_book_view(request, id):
    book = Book.objects.get(pk=id)
    return render(request, 'book_detail_view.html', {'book': book})


def authors_view(request):
    # authors = Author.objects.all()
    nazwisko = request.GET.get('nazwisko', '') #woj
    imie = request.GET.get('imie', '')
    authors = Author.objects.filter(last_name__icontains=nazwisko)
    authors = authors.filter(first_name__icontains=imie)
    return render(request, 'autor_list.html', {'object_list': authors})


def books_view(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'object_list': books})


def author_add_view(request):
    if request.method == 'GET':
        return render(request, 'add_author.html')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    year = request.POST.get('year')
    a = Author(first_name=first_name, last_name=last_name, year=year)
    a.save()
    return render(request, 'add_author.html')


def book_add_view(request):
    authors = Author.objects.all()
    genres = Genre.objects.all()
    if request.method == 'GET':
        return render(request, 'add_book.html', {'authors':authors, 'genres':genres})
    title = request.POST.get('title')
    author_id = request.POST.get('author_id')
    autor = Author.objects.get(id=author_id)
    b = Book(title=title, author=autor)
    b.save()
    gatunki = request.POST.getlist('genre')
    b.categories.set(gatunki)
    return render(request, 'add_book.html', {'authors': authors,  'genres':genres})
