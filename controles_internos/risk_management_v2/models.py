from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Risco(models.Model):
    class ClassificacaoRisco(models.TextChoices):
        BAIXO = 'BA', 'Baixo'
        MEDIO = 'ME', 'Médio'
        ALTO = 'AL', 'Alto'

    descricao = models.CharField(max_length=255)
    classificacao = models.CharField(max_length=2, choices=ClassificacaoRisco.choices)
    fator_risco = models.TextField()

class DonoControle(models.Model):
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField()
    nome_delegado = models.CharField(max_length=255)

class Controle(models.Model):
    descricao = models.CharField(max_length=255)
    dono = models.OneToOneField(DonoControle, on_delete=models.CASCADE)
    riscos = models.ManyToManyField(Risco)

class PlanoAcao(models.Model):
    class StatusPlanoAcao(models.TextChoices):
        NAO_INICIADO = 'NI', 'Não iniciado'
        EM_ANDAMENTO = 'EA', 'Em andamento'
        FINALIZADO = 'FI', 'Finalizado'

    descricao = models.TextField()
    status = models.CharField(max_length=2, choices=StatusPlanoAcao.choices)
    prazo_entrega = models.DateField()
    anexo = models.FileField(upload_to='anexos/')
    controle = models.ForeignKey(Controle, on_delete=models.CASCADE)