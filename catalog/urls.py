from django.urls import path
from . import views
from django.urls import re_path


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^autor/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    re_path(r'^author/create/$', views.AuthorCreate.as_view(), name='author-create'),
    re_path(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author-update'),
    re_path(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author-delete'),
]


