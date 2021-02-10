from django import forms
from .models import *
import datetime


class NovoLeito_Form(forms.Form):
        ala =  forms.CharField(label='Ala', max_length=5)
        leito =  forms.CharField(label='Leito', max_length=5)

class NovoPaciente_Form(forms.Form):
	nome = forms.CharField(label='Nome', max_length=50)
	cpf = forms.CharField(label='CPF:', max_length=11)
	data_nascimento = forms.DateField(label='Data de Nascimento', widget = forms.SelectDateWidget(years=range( datetime.date.today().year - 130 , datetime.date.today().year ) ))
	convenio = forms.CharField(label='Convênio', max_length=15)

class NovoInternacaoForm(forms.ModelForm):
	cpf = forms.CharField(label='CPF', max_length = 11)
	ALT_CHOICES = (('CLÍNICO', 'Clínico'), ('CIRÚRGICO', 'Cirúrgico') )
	## change the widget of the date field.
	previsao_alta  = forms.DateField(label='Previsão de Alta?', widget=forms.SelectDateWidget())
	medico = forms.CharField(label='Médico', max_length = 30) 
	situacao =  forms.ChoiceField(label='Situação',choices = ALT_CHOICES)
	dieta = forms.CharField(label='Dieta', max_length = 50)
	observacao = forms.CharField(label='Observação', max_length=200)
	def __init__(self, *args, **kwargs):
		super(NovoInternacaoForm, self).__init__(*args, **kwargs)
		## add a "form-control" class to each form input
		## for enabling bootstrap
		for name in self.fields.keys():
			self.fields[name].widget.attrs.update({
			    'class': 'form-control',
			})

	class Meta:
		model = Internacao_Paciente
		fields = ("paciente", "ala_leito")

class MoverInternacaoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MoverInternacaoForm, self).__init__(*args, **kwargs)
		## add a "form-control" class to each form input
		## for enabling bootstrap
		for name in self.fields.keys():
			self.fields[name].widget.attrs.update({
			    'class': 'form-control',
			})

	class Meta:
		model = Internacao_Paciente
		fields = ("paciente", "ala_leito")
		
		
class BoletimForm(forms.ModelForm):
	MOTIVO_CHOICES = (( 'Pneumonia Viral', 'Pneumonia Viral'), ('Suspeita de COVID-19', 'Suspeita de COVID-19'), ('Comfirmado COVID-19', 'Comfirmado COVID-19'), ('Outros', 'Outros'))
	motivo = forms.ChoiceField(label = 'Motivo da internação ', choices = MOTIVO_CHOICES)
	outros = forms.CharField(label='Outros', max_length=1000, required = False)
	STATUS_CHOICES = (( 'Acordado', 'Acordado'), ('Sonolento', 'Sonolento'), ('Em coma sem sedação', 'Em coma sem sedação'), ('Em coma com sedação', 'Em coma com sedação'))
	status = forms.ChoiceField(label = 'No momento se econtra-se ', choices = STATUS_CHOICES)
	RESPIRACAO_CHOICES = (( 'Espôntanea', 'Espôntanea'), ('Com máscara de oxigênio', 'Com máscara de oxigênio'), ('Em ventilação mecânica', 'Em ventilação mecânica'), )
	respiracao = forms.ChoiceField(label = 'Respiração ', choices = RESPIRACAO_CHOICES)
	FEBRE_CHOICES = (( 'Não', 'Não'), ('Sim', 'Sim'))
	febre = forms.ChoiceField(label = 'Febre', choices = FEBRE_CHOICES)
	antibiotico = forms.ChoiceField(label = 'Antibiótico: ', choices = FEBRE_CHOICES)
	PRESSAO_CHOICES = (( 'Alta', 'Alta'), ('Média', 'Média'), ('Baixa', 'Baixa'))
	pressao_arterial = forms.ChoiceField(label = 'Pressão Arterial ', choices = PRESSAO_CHOICES)
	pressao_arterial_med = forms.ChoiceField(label = 'Usu de medicamento de controle de pressão ', choices = FEBRE_CHOICES)
	ALIMENTACAO_CHOICES = (( 'Via oral', 'Via oral'), ('Sonda', 'Sonda'))
	alimentacao = forms.ChoiceField(label = 'Alimentação', choices = ALIMENTACAO_CHOICES)
	URINA_CHOICES = (( 'Presente', 'Presente'), ('Ausente', 'Ausente'), ('Em Hemodiálise', 'Em Hemodiálise'))
	urina =forms.ChoiceField(label = 'Urina', choices = URINA_CHOICES)
	evacuacao = forms.ChoiceField(label = 'Evacuação', choices = FEBRE_CHOICES)
	ESTADO_CHOICES = (( 'Estável', 'Estável'), ('Grave', 'Grave'), ('Gravíssimo', 'Gravíssimo'))
	estado_clinico = forms.ChoiceField(label = 'Seu estado clínico atual é', choices = ESTADO_CHOICES)	
	previsao_alta = forms.ChoiceField(label = 'Previsão de alta ', choices = FEBRE_CHOICES)
	observacao = forms.CharField(label='Observação', max_length=1000, widget=forms.Textarea)
	def __init__(self, *args, **kwargs):
		super(BoletimForm, self).__init__(*args, **kwargs)
		## add a "form-control" class to each form input
		## for enabling bootstrap
		for name in self.fields.keys():
			self.fields[name].widget.attrs.update({
				'class': 'form-control',
			})

	class Meta:
		model = Boletim_Medico_Paciente
		fields = ("paciente", )
		
class BoletimFindForm(forms.Form):
	paciente = forms.CharField(label='Paciente', max_length=50)
	cpf = forms.CharField(label='CPF', max_length = 11)