from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Usuario, Login
from .forms import Form_User, Login_Form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def login_now(request):
    if request.method == 'POST':
        form = Login_Form(request.POST)
        if form.is_valid():
            p = Login()
            p.login = form.data.get('login')
            p.senha = form.data.get('senha')
            p.save()
            return HttpResponseRedirect('/locacaoveiculos')
    else:
        form = Login_Form()
    return render(request, 'home/login.html', {'form':form})

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass


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
            user = User.objects.create_user(q.nome_usuario, q.email, q.senha)
            user.last_name = q.segundo_nome
            user.first_name = q.primeiro_nome
            user.save()
            return HttpResponseRedirect('cadastro')
    else:
        form = Form_User()
    return (form)

