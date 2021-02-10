from django import forms

class DadosPessoais_Form(forms.Form):
	nome = forms.CharField(label='nome', max_length=250)
	telefone = forms.CharField(label='telefone', max_length=15)
	email = forms.CharField(label='email', max_length=100)
