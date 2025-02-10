from django.contrib import admin
from django.urls import path,include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('musician/', include('musician.urls')),
    path('album/', include('album.urls')),
    path('', home,name='homepage'),
]
