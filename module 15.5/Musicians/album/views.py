from django.shortcuts import render,redirect
from .forms import album_forms
from .models import Albums
# Create your views here.
def albums(request):
    if request.method == 'POST':
        form = album_forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = album_forms()
    return render(request, 'album.html',{'form': form})

def edit_albums(request, id):
    album = Albums.objects.get(pk=id)
    form = album_forms(instance=album)
    if request.method == 'POST':
        form = album_forms(request.POST,instance=album)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'album.html',{'form': form})
