
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar

if settings.DEBUG:

    urlpatterns = [
        # django admin 
        path('admin/', admin.site.urls),
        
        # user management 
        path('accounts/', include('allauth.urls')),
        
            # local app 
        path('', include('bookmark.urls', namespace='bookmark')),
        path('books/', include('books.urls', namespace='books')),
        path('orders/', include('orders.urls', namespace='orders')),
        path('__debug__/', include(debug_toolbar.urls)),
        
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
