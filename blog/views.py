from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

#List of Disciplines

disciplinas = [ 'Sistema Operacional I' , 'IHC' , 'Metodologia' , ' Estrutura de Dados '
, 'Inglês IV', 'Programação WEB', 'Gestão de Projetos']

def home(request):

    data = models.Posts.objects.all()

    return render(
        request,
        'index.html',
        {
            'range': range(10),
            'disciplinas': disciplinas,
            'data': data,
        }
    )