''' since I am using django built in login and logout authentication
    there'so no need to test them because it has been tested 
    
    I will be testing the signup logic since this was a custom signup i created
'''

''' this import will allow us get the user model to work with '''
from django.contrib.auth import get_user_model

from bookmark.forms import CustomUserCreationForm

''' this import will allow us run our test '''
from django.test import TestCase

''' since it's a flow of data, this will help us test the url reverse path or route '''
from django.urls import reverse, resolve

''' the resolve import will be used to test the signupview '''
from bookmark.views import SignupPageView




    
''' define the SignupPageTests class '''
    
class SignupPageTests(TestCase):
    
    ''' test for all auth in check configuration '''
    username = 'newuser'
    email = 'newuser@email.com'
    
    ''' define the setUp fn'''
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
        
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! You should not be here, Coding gee has yout location')
        
    '''next i will test the UsercreationForm if it is being used and it resolves to signup page view'''
    def test_signup_form(self):
        ''' get the context from the form, check if the form was well created using the CUstomerUserCreationForm
            and also if csrf middleware is running which is very important 
        '''
        # form = self.response.context.get('form')
        # self.assertIsInstance(form, CustomUserCreationForm)
        # self.assertContains(self.response, 'csrfmiddlewaretoken')
        
        ''' allauth form testing  '''
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        
    ''' define the signup view for the test case '''
    def test_signup_view(self):
        view = resolve('/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )