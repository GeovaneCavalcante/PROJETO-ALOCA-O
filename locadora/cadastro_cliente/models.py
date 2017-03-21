from django.db import models

class Cadastro(models.Model):
    nome = models.CharField("Nome", max_length=100)
    cpf = models.IntegerField("CPF")
    rg = models.IntegerField("RG")
    data_hora = models.DateTimeField("Data/Hora", auto_now_add=True)

    cep = models.IntegerField("CEP")
    cidade = models.CharField("Cidade", max_length=50)
    bairro = models.CharField("Bairro", max_length=50)
    rua = models.CharField("Rua", max_length=50)
    numero = models.IntegerField("Numero")
    complemento = models.CharField("Complemento", max_length=70)


    def __str__(self):
        return self.nome