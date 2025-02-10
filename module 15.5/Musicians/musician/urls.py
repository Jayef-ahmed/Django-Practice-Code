from django.urls import path
from .views import musicians,edit_musicians,delete
urlpatterns = [
    path('', musicians, name='musicians'),
    path('edits/<int:id>', edit_musicians, name='edit_musicians'),
    path('delete/<int:id>', delete, name='delete'),
]
