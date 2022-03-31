from django.test import TestCase
from bookmark.models import BookmarkModel
# create test cases here 
class BookmarkModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ''' Set up non-modified objects used by all test methods '''
        BookmarkModel.objects.create(title = 'first test case', url='https://djangofirsttestcase.com')
        
        
    ''' this test for title label field  in BookmarkModel '''
    def test_title_label(self):
        bookmark = BookmarkModel.objects.get(pk=1)
        field_label = bookmark._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
        
    ''' this test for  url label field in BookmarkModel '''  
    def test_url_label(self):
        bookmark = BookmarkModel.objects.get(id=1)
        field_label = bookmark._meta.get_field('url').verbose_name
        self.assertEqual(field_label, 'url')
        
    ''' testing the length of the title character allowed '''
    def test_title_length(self):
        ''' Get an bookmark object to test '''
        bookmark = BookmarkModel.objects.get(pk=1)
        ''' Get the metadata for the required field and use it to query the required field data '''
        field_label = bookmark._meta.get_field('title').max_length
        ''' Compare the value to the expected result '''
        self.assertEqual(field_label, 200)
        
    ''' testing the length of the url characters allowed in the url field '''
    def test_url_length(self):
        bookmark = BookmarkModel.objects.get(pk=1)
        field_label = bookmark._meta.get_field('url').max_length
        self.assertEqual(field_label, 200)
        
    ''' testing the lenght of the choice fields '''
    def test_url_choice_length(self):
        bookmark = BookmarkModel.objects.get(id=1)
        field_label = bookmark._meta.get_field('url_choice').max_length
        self.assertEqual(field_label, 3)