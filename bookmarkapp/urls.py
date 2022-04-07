
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar



urlpatterns = [
        # admin_honeypot
        path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
        # django admin 
        path('codinggee/', admin.site.urls),
        
        # user management 
        path('accounts/', include('allauth.urls')),
        
            # local app 
        path('', include('bookmark.urls', namespace='bookmark')),
        path('books/', include('books.urls', namespace='books')),
        path('orders/', include('orders.urls', namespace='orders')),
        path('__debug__/', include(debug_toolbar.urls)),
        
    ] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
