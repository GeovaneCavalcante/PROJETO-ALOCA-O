from django.shortcuts import render

def index(request):

    return render(request, 'home/login.html')

def cadastro(request):

    return render(request, 'home/cadastro.html')