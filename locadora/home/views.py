from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Usuario
from .forms import Form_User

def index(request):

    return render(request, 'home/login.html')

def cadastro(request):
    form_rece = processando_form(request, Form_User)
    context = {
        'form_rece':form_rece,
    }
    return render(request, 'home/cadastro.html', context)

def processando_form(request, For_User):
    if request.method == 'POST':
        form = Form_User(request.POST)
        if form.is_valid():
            q = Usuario()
            q.nome_usuario = form.data.get('nome_usuario')
            q.primeiro_nome = form.data.get('primeiro_nome')
            q.segundo_nome = form.data.get('segundo_nome')
            q.email = form.data.get('email')
            q.senha = form.data.get('senha')
            q.save()
            return HttpResponseRedirect('cadastro')
    else:
        form = Form_User()
    return (form)