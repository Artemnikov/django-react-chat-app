from django.contrib import admin
from django.urls import path, include
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('server/', include('server.urls')),
    path('', include('frontend.urls')),
]
