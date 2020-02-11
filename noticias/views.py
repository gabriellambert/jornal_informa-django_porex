from django.shortcuts import render, get_object_or_404
from .models import Noticia


def index(request):
    noticias = Noticia.objects.order_by('-data_publicacao').filter(publicada=True)
    dados = {
        'noticias':noticias,
    }
    return render(request, 'index.html', dados)

def noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    noticia_selecionada = {
        'noticia': noticia,
    }
    return render(request, 'noticia.html', noticia_selecionada)
