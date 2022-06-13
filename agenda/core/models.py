from django.db import models

'''
# Contatos
- id
- nome
- telefone
- email
'''

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    ddd1 = models.CharField(max_length=2,default='')
    telefone = models.CharField(max_length=10,default='')
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome