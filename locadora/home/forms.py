from django import forms

class Form_User(forms.Form):
    nome_usuario = forms.CharField(label='nome_suario', max_length=50)
    primeiro_nome = forms.CharField(label='primeiro_nome', max_length=40)
    segundo_nome = forms.CharField(label='segundo_nome', max_length=40)
    email = forms.EmailField(label='email')
    senha = forms.CharField(label='senha', max_length=50)