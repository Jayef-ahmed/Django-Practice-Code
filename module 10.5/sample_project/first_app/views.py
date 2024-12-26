from django.shortcuts import render

# Create your views here.

def home(request):
    d = {'name' : 'Jayef Ahmed', 'Age': 23, 'friend': [
    {'name': 'salman', 'age':20},
    {'name': 'sayem', 'age': 23},
    {'name': 'ruhan', 'age': 22},
], 'course': ['python', 'c','java'],'love':"jannat"}
    return render(request, "index.html",d)