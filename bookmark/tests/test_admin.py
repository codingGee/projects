from django.contrib.auth import get_user_model
from django.test import TestCase

''' create test class below '''

class CustomUserTests(TestCase):
    
    def test_create_user(self):
        ''' assign user variable the value get_user_model '''
        User = get_user_model()
        ''' queri the user object to create a new username, email and password '''
        user = User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123'
        )
        
        ''' assert equall if username is equal to will and email is equal to will@gmail.com '''
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        
        ''' assert True if user is active '''
        self.assertTrue(user.is_active)
        
        ''' assert False if user is staff '''
        self.assertFalse(user.is_staff)
        
        ''' assert False if user is super user'''
        self.assertFalse(user.is_superuser)
        
        
        ''' def a superuser '''
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
            )
        
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)