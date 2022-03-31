''' using django simple test case '''
from django.test import SimpleTestCase
from django.urls import reverse

''' create home page test class '''

class HomepageTests(SimpleTestCase):
    
    def setUp(self):
       url = reverse('bookmark:home')
       self.response = self.client.get(url) 
    
    ''' function to test pages status code '''
    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        
    ''' testing templates '''
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'index.html')
        
    '''test for url name '''
    def test_homepage_url_name(self):
        response = self.client.get(reverse('bookmark:home'))
        self.assertEqual(response.status_code, 200)
        
    '''testing html pages if the code is correct '''
    def test_homepage_contains_correct_html(self): # new
        self.assertContains(self.response, 'Homepage')
        
    def test_homepage_does_not_contain_incorrect_html(self): # new
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
        
  
    # def test_formpage_template(self):
    #     response = self.client.post('form/')
    #     self.assertTemplateUsed(response, 'form.html')    
        
    # def test_formpage_status_code(self):
    #     response = self.client.get('form/')
    #     self.assertEqual(response.status_code, 200)
    
    # def test_form_done_page_status_code(self):
    #     response = self.client.get('form_done/')
    #     self.assertEqual(response.status_code, 200)
        
    # def test_info_page_template(self):
    #     response = self.client.get('info/')
    #     self.assertEqual(response, 'info.html')
