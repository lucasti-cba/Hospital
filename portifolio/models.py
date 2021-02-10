from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

class Post(models.Model):
	imagens = models.ImageField(upload_to='images/', blank=True,null=True)	
	nome = models.TextField(blank=False, null=False)
	texto = models.TextField(blank=False, null=False)
	data = models.DateTimeField(blank=False, null=False)
	class Meta:
		ordering = ["data"]
	def __str__(self):
		return self.nome
    

class Perfil(models.Model):
	imagens = models.ImageField(upload_to='images/', blank=True,null=True)	
	nome = models.TextField(blank=False, null=False)
	texto1 = models.TextField(blank=False, null=False)
	texto2 = models.TextField(blank=False, null=False)
	texto3 = models.TextField(blank=False, null=False)
	data = models.DateTimeField(blank=False, null=False)
	class Meta:
		ordering = ["data"]
	def __str__(self):
		return self.nome
    
class Dados_pessoais(models.Model):
	user = models.IntegerField(null=False, blank=False)
	nome = models.TextField(blank=False, null=False)
	telefone = models.TextField(blank=False, null=False)
	email = models.TextField(blank=False, null=False)
