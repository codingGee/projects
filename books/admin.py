from django.contrib import admin
from .models import Book
# Register your models here.

''' list of fields in the admin ''' 
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price",)
    
    
admin.site.register(Book, BookAdmin)
