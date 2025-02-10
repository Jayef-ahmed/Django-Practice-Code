
from django.urls import path
from .views import albums, edit_albums
urlpatterns = [
    path('', albums, name='albums'),
    path('edit/<int:id>', edit_albums, name='edit_albums'),
]
