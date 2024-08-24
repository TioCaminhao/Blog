from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def pagina(request):
    return render(request, 'index.html')

def foto(request):
    foto = foto1.objects.all()
    context = {'foto': foto}
    return render(request, 'foto.html', context)

def sobremim(request, *args, **kwargs):
    sobremim = sobremim1.objects.all() 
    context={'sobremim': sobremim}
    return render(request, 'sobremim.html', context)

def dados(request, *args, **kwargs):
    dados = dados1.objects.all() 
    context={'dados': dados}
    return render(request, 'dados.html', context)