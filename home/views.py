from home.models import Chave
from django.shortcuts import render
from django.contrib import messages

def index(request):
    dados = Chave.objects.order_by('nome').filter(
        mostrar=True
    )
    return render(request, 'home/index.html', {'dados':dados})

def reservar(request, xid):
    nome = request.POST.get('name')
    edv = request.POST.get('edv')

    if nome != '' and edv != '':
        chave = Chave.objects.get(id=xid)
        chave.usuario_nome = nome
        chave.usuario_edv = edv
        chave.status = 'I'

        chave.save()
        messages.add_message(request,messages.SUCCESS,'Chave reservada com sucesso!')
    else:
        messages.add_message(request,messages.ERROR,'Digite valores nos campos!')
        
    dados = Chave.objects.order_by('-id').filter(
        mostrar=True
    )
    return render(request, 'home/index.html', {'dados':dados})

def devolver(request, xid):
    edv = request.POST.get('edv')

    chave = Chave.objects.get(id=xid)

    if edv == chave.usuario_edv:

        chave.usuario_nome = ''
        chave.usuario_edv = ''
        chave.status = 'D'

        chave.save()
        dados = Chave.objects.order_by('-id').filter(
            mostrar=True

        )
        messages.add_message(request,messages.SUCCESS,'Chave devolvida com sucesso!')
        return render(request, 'home/index.html', {'dados':dados})
    else:
        dados = Chave.objects.order_by('-id').filter(
            mostrar=True
        )
        messages.add_message(request,messages.ERROR,'EDV incorreto. Chave não devolvida!')
        return render(request, 'home/indisponiveis.html', {'dados':dados})

def indisponiveis(request):
    dados = Chave.objects.order_by('nome').filter(
        mostrar=True
    )
    return render(request, 'home/indisponiveis.html', {'dados':dados})

def about(request):

    return render(request, 'home/about.html')

