''' import django user admin '''
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import BookmarkModel

''' import Admin user model'''
from django.contrib.auth import get_user_model
''' import forms for cUstom UserAdmin '''
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()

''' create CustomUserAdmin class '''
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)

''' this is to register the admin model display in the admin panel '''
@admin.register(BookmarkModel)

# create admin class for admin data population 
class AdminBookmark(admin.ModelAdmin):
    # list_display of the information to store and search
    list_display = ('title', 'url', 'url_choice', 'date')
    search_fields = ('title', 'url', 'date')
    
