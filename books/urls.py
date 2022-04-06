from django.urls import path
from .views import BookListView, BookDetailView, SearchResultListView


app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<uuid:pk>', BookDetailView.as_view(), name="book-detail"),
    path('search/', SearchResultListView.as_view(), name="search-results"),
]
