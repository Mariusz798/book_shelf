from django.shortcuts import render

# Create your views here.
from books.models import Author, Book


def index(request):
    return render(request, 'base.html')


def detail_author_view(request, id):
    author = Author.objects.get(pk=id)
    return render(request, 'author_detail_view.html', {'author': author})


def authors_view(request):
    authors = Author.objects.all()
    return render(request, 'object_list.html', {'object_list': authors})


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
