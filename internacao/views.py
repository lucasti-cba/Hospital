from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from .models import *
from .forms import *
import os
import time
from django.template import Library
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime
from django import template


# Create your views here.
@login_required
def add_Ala(request):
    form = NovoLeito_Form()
    if request.method == 'POST':
        form = NovoLeito_Form(request.POST)
        if form.is_valid():
            ala = form.cleaned_data['ala']
            leito = form.cleaned_data['leito']
            Ala = Ala_Leito(ala = ala, leito = leito, situacao = 'LIVRE' , cor = 'CINZA')
            Ala.save()
            return redirect('internacao')
    return render(request, 'add_ala.html', {'form':form})

@login_required
def internacao(request):
    internados = Ala_Leito.objects.all()
    inters = Internacao_Paciente.objects.filter(alta__isnull=True)
    clinico = 0
    cirurgico = 0
    for inter in internados:
        if inter.situacao ==  'CLÍNICO': clinico += 1
        elif inter.situacao == 'CIRÚRGICO': cirurgico += 1
    return render(request, 'internacao.html', {'internados':internados,'cirurgico':cirurgico,'inters':inters, 'clinico':clinico,})

@login_required
def novoPaciente(request):
    form = NovoPaciente_Form()
    if request.method == 'POST':
        form = NovoPaciente_Form(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            cpf = form.cleaned_data['cpf']
            data_nascimento = form.cleaned_data['data_nascimento']
            convenio = form.cleaned_data['convenio']
            paciente = Paciente(nome = nome, cpf = cpf, data_nascimento = data_nascimento, convenio = convenio)
            paciente.save()
            return redirect('internacao')
    return render(request, 'novo_paciente.html', {'form':form})

@login_required
def novoInternacao(request):
    pacientes_jquery = Paciente.objects.all()
    form = NovoInternacaoForm()
    if request.method == 'POST':
        form = NovoInternacaoForm(request.POST)
        if form.is_valid():
            paciente = form.cleaned_data['paciente']
            cpf = form.cleaned_data['cpf']
            ala_leito = form.cleaned_data['ala_leito']
            previsao_alta = form.cleaned_data['previsao_alta'] 
            medico = form.cleaned_data['medico']
            situacao = form.cleaned_data['situacao']
            dieta = form.cleaned_data['dieta']
            observacao = form.cleaned_data['observacao']
            paciente = get_object_or_404(Paciente, nome = paciente, cpf = cpf)
            ala_leito = get_object_or_404(Ala_Leito, id = ala_leito.id )
            ala_leito.situcao = situacao
            if situacao == 'CLÍNICO':
                ala_leito.cor = 'AZUL'
                ala_leito.situacao = situacao
            elif situacao == 'CIRÚRGICO':
                ala_leito.cor = 'VERDE'
                ala_leito.situacao = situacao
            ala_leito.save()
            internacao = Internacao_Paciente(paciente = paciente, data_entrada = datetime.now(), previsao_alta = previsao_alta, ala_leito = ala_leito, medico = medico, dieta = dieta, observacao = observacao)
            internacao.save()
            return redirect('internacao')
    return render(request, 'novo_internacao.html', {'pacientes_jquery':pacientes_jquery, 'form':form})


@login_required
def altaInternacao(request, internacao):
	internacao = get_object_or_404(Internacao_Paciente, id = internacao)
	internacao.alta = datetime.now()
	ala_leito = get_object_or_404(Ala_Leito, id=internacao.ala_leito.id )
	ala_leito.situacao = 'LIVRE'
	ala_leito.cor = 'CINZA'
	internacao.save()
	ala_leito.save()
	return redirect('internacao')
	
@login_required
def moverInternacao(request, internacao):
	ala_leito_jquery = Ala_Leito.objects.all()
	paciente = get_object_or_404(Internacao_Paciente, id = internacao)
	form = MoverInternacaoForm()
	if request.method == 'POST':
		form = MoverInternacaoForm(request.POST)
		if form.is_valid():
			ala_leito = form.cleaned_data['ala_leito']
			internacao = get_object_or_404(Internacao_Paciente, id = internacao)
			clean_leito = get_object_or_404(Ala_Leito, id = internacao.ala_leito.id )
			temp = clean_leito.situacao
			clean_leito.situacao = 'LIVRE'
			clean_leito.cor = 'CINZA'
			clean_leito.save()
			ala_leito.situacao = temp
			if temp == 'CLÍNICO':
				ala_leito.cor = 'AZUL'
			elif temp == 'CIRÚRGICO':
				ala_leito.cor = 'VERDE'
			ala_leito.save()
			internacao.ala_leito = ala_leito
			internacao.save()
			return redirect('internacao')
	return render(request, 'mover_internacao.html', {'form':form, 'paciente':paciente, 'ala_leito_jquery':ala_leito_jquery})
	
@login_required
def reservarLeito(request, leito):
	internacao = get_object_or_404(Ala_Leito, id = leito)
	internacao.situacao = 'RESERVADO'
	internacao.cor = 'LARANJA'
	internacao.save()
	return redirect('internacao')

@login_required
def cancelarReserva(request, leito):
	internacao = get_object_or_404(Ala_Leito, id = leito)
	internacao.situacao = 'LIVRE'
	internacao.cor = 'CINZA'
	internacao.save()
	return redirect('internacao')

@login_required
def boletim(request):	
	form = BoletimForm()
	if request.method == 'POST':
		form = BoletimForm(request.POST)
		if form.is_valid():
			paciente = form.cleaned_data['paciente']
			internacao = get_object_or_404(Internacao_Paciente, paciente = paciente , alta__isnull = True)
			data_evolucao = datetime.now()
			liberacao  = datetime.now()
			motivo = form.cleaned_data['motivo']
			outros = form.cleaned_data['outros']
			status = form.cleaned_data['status']
			respiracao = form.cleaned_data['respiracao']
			febre = form.cleaned_data['febre']
			antibiotico = form.cleaned_data['antibiotico']
			pressao_arterial = form.cleaned_data['pressao_arterial']
			pressao_arterial_med = form.cleaned_data['pressao_arterial_med']
			alimentacao = form.cleaned_data['alimentacao']
			urina = form.cleaned_data['urina']
			evacuacao = form.cleaned_data['evacuacao']
			estado_clinico = form.cleaned_data['estado_clinico']
			previsao_alta = form.cleaned_data['previsao_alta']
			observacao = form.cleaned_data['observacao']
			if motivo == 'OUTROS': motivo = outros
			boletim = Boletim_Medico_Paciente(paciente = paciente, internacao = internacao,	data_evolucao = data_evolucao, liberacao = liberacao, motivo = motivo, respiracao = respiracao, febre = febre, antibiotico = antibiotico, pressao_arterial = pressao_arterial, pressao_arterial_med = pressao_arterial_med, alimentacao = alimentacao, urina = urina, evacuacao = evacuacao, estado_clinico = estado_clinico, previsao_alta = previsao_alta, observacao = observacao )
			boletim.save()
			return redirect('internacao')
	return render(request, 'boletim.html', {'form':form})

def boletim_find(request):
	form = BoletimFindForm()
	return render(request, 'boletim_find.html', {'form':form})