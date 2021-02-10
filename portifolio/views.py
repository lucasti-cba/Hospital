# -*- coding: cp1252 -*-

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



def index(request):
        posts = Post.objects.all()
        perfil = get_object_or_404(Perfil, nome = 'Web Alive')
        print(perfil.imagens)
        index = True
        return render(request,'index.html', {'posts': posts, 'perfil':perfil, 'index':index})


def cadastrar_usuario(request):
	if request.method == "POST":
	    form_usuario = UserCreationForm(request.POST)
	    if form_usuario.is_valid():
	        form_usuario.save()
	        username = form_usuario.cleaned_data['username']
	        password = form_usuario.cleaned_data['password1']
	        usuario = authenticate(request, username=username, password=password)
	        if usuario is not None:
	            auth_login(request, usuario)
	            return redirect('dadospessoais')
	    else:
	    	return render(request, 'cadastro_user.html', {'form': form_usuario, 'title': 'Criar Conta', })

	form = UserCreationForm()	
	return render(request, 'cadastro_user.html', {'form': form, 'title': 'Criar Conta', })




def logar_usuario(request):
    mensagem = None 
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            auth_login(request, usuario)
            user = request.user.id
            try:
	            dados = Dados_pessoais.objects.get(user=user)	         
	            return redirect('index')
            except:
            	return redirect('dadospessoais')
        else:
        	mensagem = 'Usuario ou senha invalido.'
    return render(request, 'user_login.html', {'mensagem':mensagem, 'title':'Login', })




def logout(request):
    auth_logout(request)
    return redirect('index')


@login_required
def dadospessoais(request):
	user = request.user.id
	if request.method == "POST":
		form = DadosPessoais_Form(request.POST)
		if form.is_valid():
			try:
				dados = Dados_pessoais.objects.filter(user=user)
				nome = form.cleaned_data['nome']
				telefone = form.cleaned_data['telefone']
				dadosP = Dados_pessoais(id=dados[0].id, user=user,nome=nome, telefone=telefone, email=email)
				dadosP.save()
				return redirect("index")
			except:
				nome = form.cleaned_data['nome']
				telefone = form.cleaned_data['telefone']
				email = form.cleaned_data['email']
				dadosP = Dados_pessoais(user=user,nome=nome, telefone=telefone, email=email)
				dadosP.save()
				usern = request.user
				usern.save()
				return redirect("index")
	try:
		dados = Dados_pessoais.objects.filter(user=user)
		if dados[0] is None:
			pass
		form = DadosPessoais_Form()
		return render(request, 'dadospessoais.html', {'form': form, 'dados': dados[0], 'title': 'Editar Dados Pessais'})
	except:
		pass
	form = DadosPessoais_Form()
	return render(request, 'dadospessoais.html', {'form': form, 'title': 'Editar Dados Pessais', })
