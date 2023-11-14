from django.shortcuts import render
from . import models

# Create your views here.
def all(request):
        berita = models.berita.objects.all()
        context = {'beritas' : berita}
        return render(request, 'menu/all.html',context)

def trending(request):
        return render(request, 'menu/trending.html')

def sports(request):
        return render(request, 'menu/sports.html')

def politics(request):
        return render(request, 'menu/politics.html')

def lifeStyle(request):
        return render(request, 'menu/lifeStyle.html')

def entertaiment(request):
        return render(request, 'menu/entertaiment.html')

def healty(request):
        return render(request, 'menu/healty.html')