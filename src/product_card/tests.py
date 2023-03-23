from django.test import TestCase
from django.urls import reverse
from product_card.models import Book
from datetime import date
from references.models import BookAuthor

class BookTestCase(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            name='Test Book',
            publishing_year='2022',
            pages=250,
            binding='Hardcover',
            format='A5',
            isbn='9783161484100',
            weight=500,
            age_restriction=18,
            date_of_addition=date.today(),
            description='Test Description',
        )
    def test_book_model(self):
        self.assertEqual(str(self.book), 'Test Book')

    def test_book_list_view(self):
        url = reverse('product_card:pc_list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_book_detail_view(self):
        url = reverse('product_card:pc_detail', kwargs={'pk': self.book.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_book_update_view(self):
        url = reverse('product_card:pc_update', kwargs={'pk': self.book.pk})
        author1 = BookAuthor.objects.create(name='Test Author 1')
        author2 = BookAuthor.objects.create(name='Test Author 2')
        resp = self.client.post(url, {
            'name': 'Updated Test Book',
            'publishing_year': '2023',
            'pages': 300,
            'binding': 'Softcover',
            'format': 'A4',
            'isbn': '9783161484101',
            'weight': 600,
            'age_restriction': 21,
            'date_of_addition': date.today(),
            'description': 'Updated Test Description',
            'author': [author1.pk, author2.pk],
        })
        self.assertRedirects(resp, reverse('product_card:pc_detail', kwargs={'pk': self.book.pk}))
        self.book.refresh_from_db()
        self.assertEqual(self.book.name, 'Updated Test Book')
        self.assertEqual(self.book.author.count(), 2)
        self.assertEqual(self.book.author.first(), author1)
        self.assertEqual(self.book.author.last(), author2)

    def test_book_delete_view(self):
        url = reverse('product_card:pc_delete', kwargs={'pk': self.book.pk})
        resp = self.client.post(url)
        self.assertRedirects(resp, reverse('product_card:pc_list'))
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

    def test_book_create_view(self):
        url = reverse('product_card:pc_create')
        author = BookAuthor.objects.create(name='Author Name', surname='Author Surname')
        resp = self.client.post(url, {
            'name': 'New Test Book',
            'publishing_year': '2024',
            'pages': 350,
            'binding': 'Hardcover',
            'format': 'A5',
            'isbn': '9783161484102',
            'weight': 700,
            'age_restriction': 18,
            'date_of_addition': date.today(),
            'description': 'New Test Description',
            'author': [author.pk],
        })
        self.assertRedirects(resp, reverse('product_card:pc_detail', kwargs={'pk': Book.objects.latest('id').pk}))
        self.assertTrue(Book.objects.filter(name='New Test Book').exists())