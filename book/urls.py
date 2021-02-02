from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('home/', views.BookHome.as_view(), name='book_home'),
    # path('list/', views.book_list, name='book_list'),
    path('list/', views.BookListView.as_view(), name='book_list'),
    path('list/authors/', views.author_list, name='authors_list'),
    path('search_book/', views.search_book, name='search_book'),
    # path('<slug:slug_field>/', views.book_detail, name='book_detail'),
    path('<slug:slug>/', views.BookDetailView.as_view(), name='book_detail'),
    path('author/<int:author_id>/', views.book_by_author, name='by_author'),
]
