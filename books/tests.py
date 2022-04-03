from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
''' import models '''
from .models import Book, Review

# Create your tests here.

class BookTests(TestCase):
    
    def setUp(self):
        ''' setup for reviews '''
        self.user = get_user_model().objects.create_user(
            username = 'reviewuser',
            email = 'reviewuser@email.com',
            password = 'testpass123'
        )
        
        ''' setup for books '''
        self.book = Book.objects.create(
            title = 'Harry Potter',
            author = 'JK Rowlings',
            price = '25.00',
        )
        
        self.review = Review.objects.create(
            book = self.book,
            author = self.user,
            review = 'An excellent review'
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowlings')
        self.assertEqual(f'{self.book.price}', '25.00')
        
    def test_book_list_view(self):
        response = self.client.get(reverse('books:book-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')
        
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(no_response, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'An excellent review')
        self.assertTemplateUsed(response, 'books/book_detail.html')
