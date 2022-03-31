from django.db import models
from django.utils.translation import gettext_lazy  as _
from django.contrib.auth.models import AbstractUser


''' create an abstract User ''' 
class CustomUser(AbstractUser):
    pass

''' Create your models here '''
class BookmarkModel(models.Model):
    # model information for process
    PRIVATE = 'PR'
    PUBLIC = 'PB'
    # create choices dictionary
    URL_CHOICES = [
        (PRIVATE, 'private'),
        ( PUBLIC, 'public'),
    ]
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    url_choice = models.CharField(max_length=3, choices=URL_CHOICES, default='pick one')
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'boomark'
        ordering = ['title']
        
    def is_upperclass(self):
        return self.url_choice in {
            self.PRIVATE, self.PUBLIC
        }