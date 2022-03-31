''' importing Model form from Django Form '''
from django.forms import ModelForm

''' importing BookmarkModel from Model file '''
from .models import BookmarkModel

''' from django i'm importing usercreationform and userchange form to create the admin user form '''
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

''' import django default user admin model '''
from django.contrib.auth import get_user_model

''' create a custom user admin form '''
class CustomUserCreationForm(UserCreationForm):
    
    '''  use the get_user_model '''
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
        
''' create a Custom Use rChange Form '''
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username')

'''  Creating Form from ModelForm '''
class BookmarkForm(ModelForm):
    
    class  Meta:
        # call the form model for the form 
        model = BookmarkModel
        # form display
        fields = ['title', 'url', 'url_choice' ]
        