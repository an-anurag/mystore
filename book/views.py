# _*_ encoding utf-8 _*_

""" views for book app """

from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView

from .models import Author, Book


class BookHome(TemplateView):
    template_name = 'book/home.html'

    def get_context_data(self, **kwargs):
        context = super(BookHome, self).get_context_data(**kwargs)
        context['recent'] = Book.objects.filter(is_active=True).order_by('-created_on')[:3]
        context['total'] = Book.total_books()
        return context


def author_list(request):
    if request.method == 'GET':
        all_authors = Author.objects.all
        context = {'authors': all_authors, }
        return render(request, 'book/author_list.html', context)
    return render(request, 'book/author_list.html')


class BookListView(ListView):
    model = Book
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        book = self.object
        context['related'] = Book.objects.filter(genre=book.genre).exclude(title=book.title)
        return context


def search_book(request):
    if request.method == "GET":
        query = request.GET.get('query', None)
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) |
            Q(authors__first_name__icontains=query) | Q(authors__last_name__icontains=query)
        ).distinct()
        return render(request, 'book/book_list.html', {'books': books, 'query': query})


def book_by_author(request, author_id=None):
    author = Author.objects.get(pk=author_id)
    books = Book.objects.filter(authors__id=author_id)
    return render(request, 'book/book_list.html', {'books': books, 'author': author})