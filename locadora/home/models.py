from django.db import models

class Usuario(models.Model):
    nome_usuario = models.CharField("Nome de Usuario ", max_length=50)
    primeiro_nome = models.CharField("Primeiro Nome", max_length=40)
    segundo_nome = models.CharField("Segundo Nome", max_length=40)
    email = models.EmailField("Email")
    senha = models.CharField("Senha", max_length=50)

    def __str__(self):
        return (self.nome_usuario)
class Login(models.Model):
    login = models.CharField("Login", max_length=50)
    senha = models.CharField("Senha", max_length=50)

    def __str__(self):
        return self.login