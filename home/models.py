from django.db import models

class Chave(models.Model):
    nome = models.CharField(max_length=50)
    usuario_nome = models.CharField(max_length=50, default='', null=True, blank=True)
    usuario_edv = models.CharField(max_length=8, default='', null=True, blank=True)
    status = models.CharField(max_length=10, default='D', choices=(
        ('D', 'Disponível'),
        ('I', 'Indisponível'),
    ))
    color = models.CharField(max_length=20, null=True, blank=True)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome