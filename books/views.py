from django.http import HttpResponse
from django.shortcuts import render, redirect

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
    nazwisko = request.GET.get('nazwisko', '')
    imie = request.GET.get('imie', '')
    authors = Author.objects.filter(last_name__icontains=nazwisko)
    authors = authors.filter(first_name__icontains=imie)
    return render(request, 'autor_list.html', {'object_list': authors})


def books_view(request):
    # books = Book.objects.all()
    authors = Author.objects.all()
    title = request.POST.get('title', '')
    author_id = request.POST.get('author_id')
    books = Book.objects.filter(title__icontains=title)
    if author_id is not None:
        books = books.filter(author_id=author_id)
    return render(request, 'book_list.html', {'object_list': books, 'authors': authors})


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
        return render(request, 'add_book.html', {'authors': authors, 'genres': genres})
    title = request.POST.get('title')
    author_id = request.POST.get('author_id')
    autor = Author.objects.get(id=author_id)
    b = Book(title=title, author=autor)
    b.save()
    gatunki = request.POST.getlist('genre')
    b.categories.set(gatunki)
    return render(request, 'add_book.html', {'authors': authors, 'genres': genres})


def create_session(request):
    if request.method == 'GET':
        return render(request, 'show_session.html', {"sessions": request.session})
    key = request.POST['key']
    val = request.POST['value']
    request.session[key] = val
    return render(request, 'show_session.html', {"sessions": request.session})


def create_cookies(request):
    if request.method == 'GET':
        return render(request, 'show_session.html', {"sessions": request.COOKIES})
    key = request.POST['key']
    val = request.POST['value']
    httpResponse = render(request, 'show_session.html', {"sessions": request.COOKIES})
    httpResponse.set_cookie(key, val)
    return httpResponse


def set_session(request):
    request.session['counter'] = 0
    return render(request, 'set_session.html')


def show_session(request):
    try:
        request.session['counter'] += 1
        counter = request.session['counter']
    except:
        counter = 0
    return render(request, 'show2_session.html', {'counter': counter})


def del_session(request):
    try:
        del request.session['counter']
        return render(request, 'del_session.html', {'msg': 'udało sie skasować'})
    except:
        return render(request, 'del_session.html', {'msg': "nie udało sie skasowas bo nie było"})


def login(request):
    if request.method == 'GET':
        zalogowany = request.session.get('loggedUser', '')
        return render(request, 'form_to_login.html', {'logged': zalogowany})
    elif request.method == 'POST':
        name = request.POST.get('name')
        request.session['loggedUser'] = name

    return render(request, 'form_to_login.html', {'logged': name})


def add_to_session(request):
    if request.method == 'GET':
        return render(request, 'form_add_to_session.html')
    elif request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        request.session[key] = value
        return render(request, 'add_to_session.html', {'key': key, 'value': value})


def show_all_session(request):
    try:
        return render(request, 'show_all_session.html', {'sessions': request.session})
    except:
        return HttpResponse(request, 'Brak danych do wyświetlenia')


def set_cookie(request):
    if request.method == 'GET':
        return render(request, 'set_cookie.html')
    name = request.POST.get('name')
    response = render(request, 'set_cookie.html')
    response.set_cookie('User', name)
    return response


def show_cookie(request):
    if 'User' in request.COOKIES:
        return render(request, 'show_cookie.html', {'user': request.COOKIES.get('User')})
    else:
        return render(request, 'msg.html', {'command': 'wyświetlenia.'})


def del_cookie(request):
    if 'User' in request.COOKIES:
        response = render(request, 'del_cookie.html')
        response.delete_cookie('User')
        return response
    else:
        return render(request, 'msg.html', {'command': 'usunięcia.'})


def add_to_cookie(request):
    if request.method == 'GET':
        return render(request, 'form_add_cookie.html')
    elif request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        response = redirect("/show_all_cookie/")
        response.set_cookie(key, value)
        return response


def show_all_cookie(request):
    try:
        return render(request, 'show_all_cookie.html', {'cookies': request.COOKIES})
    except:
        return render(request, 'msg.html', {'command': 'wyświetlenia.'})
