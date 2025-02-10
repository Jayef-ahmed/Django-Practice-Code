from django.shortcuts import render
from album.models import Albums
# Create your views here.
def home(req):
    data = Albums.objects.all()
    return render(req, 'home.html', {'data': data})