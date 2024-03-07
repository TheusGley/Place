from django.db import models
from django.contrib.auth.models import User

status_choices = [
("Confirmado", "Confirmado"),
("Cancelado", "Cancelado"),

    
]
servicos_choices = [
("Disponivel", "Disponivel"),
("Indisponivel", "Indisponivel"),

    
]

class Servico (models.Model):
    
    nome_servico =  models.CharField(max_length=100)
    colaborador = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'servico_colaborador')
    status = models.CharField(max_length=20, choices= servicos_choices)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    notas = models.CharField(max_length=100)
    
    def __str__(self) :
        return self.nome_servico
    
    




class Agendamento (models.Model):
    servico =  models.ForeignKey(Servico, on_delete = models.CASCADE)
    status =  models.CharField(max_length=20, choices= status_choices)
    data = models.DateField( auto_now=False, auto_now_add=False)
    hora = models.TimeField()
    cliente = models.ForeignKey(User, on_delete= models.CASCADE,related_name='agenda_cliente')
    colaborador = models.ForeignKey(User, on_delete= models.CASCADE, related_name='agenda_colaborador')
    notas = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.cliente.username
        
        
