
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # django admin 
    path('admin/', admin.site.urls),
    
    # user management 
    path('accounts/', include('allauth.urls')),
    
        # local app 
    path('', include('bookmark.urls', namespace='bookmark')),
    path('books/', include('books.urls', namespace='books')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
