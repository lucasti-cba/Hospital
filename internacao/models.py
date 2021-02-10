from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.TextField(blank =False, null=False, unique=False)
    cpf = models.TextField(blank = True, null= True , unique=True)
    data_nascimento = models.DateField(blank=True, null=True)
    convenio = models.TextField(blank=False, null=False, unique=False)
    def __str__(self):
        return self.nome


class Ala_Leito(models.Model):
    leito = models.TextField(blank=False, null=False, unique=False)
    ala = models.TextField(blank=False, null=False, unique=False)	
    situacao = models.TextField(blank=True, null=True, unique=False)
    cor = models.TextField(blank=True)
    class Meta:
        ordering = ["ala", "leito"]
    def __str__(self):
        return self.ala + self.leito

class Internacao_Paciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True)
    data_entrada = models.DateTimeField(blank=False, null=False)
    previsao_alta = models.DateTimeField(blank=False, null=False)
    alta = models.DateTimeField(blank=False, null=True)
    ala_leito = models.ForeignKey(Ala_Leito, on_delete=models.CASCADE, blank=True, null=True)
    medico = models.TextField(blank=True, null=True, unique=False)
    dieta = models.TextField(blank=True, null=True, unique=False)
    observacao = models.TextField(blank=True, null=True, unique=False)
 

class Boletim_Medico_Paciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True)
    internacao = models.ForeignKey(Internacao_Paciente, on_delete=models.CASCADE, blank=True, null=True)
    data_evolucao  = models.DateTimeField(blank=False, null=False)
    liberacao  = models.DateTimeField(blank=False, null=False)
    motivo = models.TextField(blank=False, null=False, unique=False)
    status = models.TextField(blank=False, null=False, unique=False)
    respiracao = models.TextField(blank=False, null=False, unique=False)
    febre = models.TextField(blank=False, null=False, unique=False)
    antibiotico = models.TextField(blank=False, null=False, unique=False)
    pressao_arterial = models.TextField(blank=False, null=False, unique=False)
    pressao_arterial_med = models.TextField(blank=False, null=False, unique=False)
    alimentacao = models.TextField(blank=False, null=False, unique=False)
    urina = models.TextField(blank=False, null=False, unique=False)
    evacuacao = models.TextField(blank=False, null=False, unique=False)
    estado_clinico = models.TextField(blank=False, null=False, unique=False)
    previsao_alta = models.TextField(blank=True, null=True, unique=False)
    observacao = models.TextField(blank=False, null=False, unique=False)
    
    
    
    
