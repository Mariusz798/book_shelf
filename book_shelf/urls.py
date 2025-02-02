"""book_shelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("author_list/", views.authors_view),
    path("author/<int:id>/", views.detail_author_view),
    path("book/<int:id>/", views.detail_book_view),
    path("book_list/", views.books_view),
    path("author_add/", views.author_add_view),
    path("book_add/", views.book_add_view),
    path("create_session/", views.create_session),
    path("cookies/", views.create_cookies),
    path("set_session/", views.set_session),
    path("show_session/", views.show_session),
    path("del_session/", views.del_session),
    path('login/', views.login),
    path('add_to_session/', views.add_to_session),
    path('show_all_session/', views.show_all_session),
    path('set_cookie/', views.set_cookie),
    path('show_cookie/', views.show_cookie),
    path('del_cookie/', views.del_cookie),
    path('add_to_cookie/', views.add_to_cookie),
    path('show_all_cookie/', views.show_all_cookie),

]

