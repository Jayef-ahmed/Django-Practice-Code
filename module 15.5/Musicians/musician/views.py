from django.shortcuts import render,redirect
from .forms import musician_forms
from .models import Musician
# Create your views here.
def musicians(request):
    if request.method == 'POST':
        form = musician_forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musicians')
    else:
        form = musician_forms()
    return render(request, 'music.html',{'form': form})

def edit_musicians(request, id):
    musician = Musician.objects.get(pk=id)
    form = musician_forms(instance=musician)
    if request.method == 'POST':
        form = musician_forms(request.POST,instance=musician)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'music.html',{'form': form})

def delete(request, id):
    musician = Musician.objects.get(pk=id)
    musician.delete()
    return redirect('homepage')