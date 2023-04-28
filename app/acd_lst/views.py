from re import S
from django.shortcuts import render, redirect
from .forms import ObitoForm, ListForm, UploadFileForm, List
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from acd_app.settings import DEBUG
from src.file_handler import handle_uploaded_file

from src.verificacpf import validarCPF, formater
from src.acd_tabelas import postar_tabelas_indices
from src.serprosoap import buscarDataObito
from src.serprosoap import buscarFichaFinanceira


from .models import *

#import pandas as pd 


#function to handle an uploaded file.
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("#=======upload_file===========")
            print("#-----request.FILES-----------")
            print(request.FILES['file'])
            print(request.path)
        	#print(UploadedFile().content_type)
            handle_uploaded_file(request.FILES['file'])
        	#return HttpResponseRedirect('upload/')
            return render(request, 'upload_home.html', {})
    else:

        form = UploadFileForm()
    return render(request, 'upload_home.html', {'form': form})


def ficha(request):

	if DEBUG:
		print("** FICHA FINANCEIRA **")
	
	if request.method == "POST":
		x = request.POST.get('numero_cpf')
		#print("---")
		#print (x)
		#print('---')

	first_name = "DCP"
	last_name = "Brasília-DF"
	return render(request,'ficha.html',{'first_name':first_name,'last_name':last_name})

def fichalista(request):
	
	import json
	
	listacpf = {} #dicionário {'id':id,'cpf':cpf, 'nome':nome, 'dataobito':data}
	lista_validos = []
	lista_invalidos = []
	total_invalidos =0
	total_validos = 0
	
	bruto,desconto,liquido = [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]
	totbruto,totdesc,totliq = 0,0,0
	print ("** FICHA FINANCERIA LISTA **")

	if request.method == "POST":
		_cpf = request.POST.get('cpf')
		_anoi = request.POST.get('anoinicial')
		_anof = request.POST.get('anofinal')
		
		#print (_cpf, _anoi, _anof)
		
		listacpf = validarCPF(_cpf) 
		
		#print (listacpf)
		lista_validos = listacpf['validos']
		#print (lista_validos)

		fichas = buscarFichaFinanceira(lista_validos,_anoi,_anof)		

	return render(request,'ficha-lista.html',{'fichas':fichas, 'bruto':bruto,'desconto':desconto,'liquido':liquido})



def extrator(request):

	if DEBUG:
		print("** EXTRATOR **")
	
	if request.method == "POST":
		x = request.POST.get('numero_cpf')
		#print("---")
		#print (x)
		#print('---')

	first_name = "DCP"
	last_name = "Brasília-DF"
	return render(request,'extrator.html',{'first_name':first_name,'last_name':last_name})


def extratorlista(request):
	import json
	
	listacpf = {} #dicionário {'id':id,'cpf':cpf, 'nome':nome, 'dataobito':data}
	lista_validos = []
	lista_invalidos = []
	total_invalidos =0
	total_validos = 0
	
	bruto,desconto,liquido = [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]
	totbruto,totdesc,totliq = 0,0,0
	print ("** EXTRATOR LISTA **")

	if request.method == "POST":
		_cpf = request.POST.get('cpf')
		_anoi = request.POST.get('anoinicial')
		_anof = request.POST.get('anofinal')
		
		#print (_cpf, _anoi, _anof)
		
		listacpf = validarCPF(_cpf) 
		
		#print (listacpf)
		lista_validos = listacpf['validos']
		#print (lista_validos)

		fichas = buscarFichaFinanceira(lista_validos,_anoi,_anof)		

	return render(request,'extrator-lista.html',{'fichas':fichas, 'bruto':bruto,'desconto':desconto,'liquido':liquido})




def obitoslista(request):

	""" 
	listacpf {
		'id': id,
		'cpf': cpf,
		'nome': nome,
		'dataobito': data
	}
	"""
	listacpf = {} 
	lista_validos = []
	lista_invalidos = []
	total_invalidos =0
	total_validos = 0
	items = {}
	msg = ''

	if DEBUG:
		print("** OBITOS-LISTA **")

	if request.method == "POST":
		
		form = ObitoForm(request.POST, request.FILES)

		x = request.POST.get('numero_cpf')
		y = request.POST.get('varios_cpf')
			
		# x é uma string simples e y é uma lista. Caso ambos os formulários contenham dados
		if len(x) > len(y):
			listacpf = validarCPF(x)
		else:
			listacpf = validarCPF(y)


		lista_validos = listacpf['validos']
		total_validos = len(lista_validos)
		lista_invalidos = listacpf ['invalidos']
		total_invalidos = len(lista_invalidos)

		#print("#-------------def-obitoslista---------------------")
		#print ("# x: ", x)
		#print ("# y: ", y)
		#print ("# z: ", z)		
		#print("#-------------------------------------------------")
		
		if x=='' and y == '':
			messages.success (request, ('Você deve inserir pelo menos um CPF para pesquisar'))


		if total_invalidos > 1:
			msg = str(total_invalidos) + ' CPFs inválidos.'
			messages.success (request, (msg))
		else:
			if total_invalidos == 1:
				msg = str(total_invalidos) + ' CPF inválido.'
				messages.success (request, (msg)) 

		#print ('cpf válidos:',lista_validos) 
		items = buscarDataObito(lista_validos)
		#print (items)	
		return render(request,'obitos-lista.html',{'items':items})

		

		"""
		if form.is_valid():
			messages.success (request, ('Dados enviados'))
			contexto = { 'form':form}
			return render(request,'obitos-lista.html',contexto)
		else:
			messages.success (request, ('Foi gerado um arquivo com CPF inválidos'))
			contexto = {'form': form}
			return render(request, 'obitos-lista.html',contexto)
		"""

	else:
		form = ObitoForm()
		contexto = {'form': form}
		#return HttpResponseRedirect('/obitos-lista')
		return render(request, 'obitos-lista.html',contexto)

	
def obitos(request):
		
	form = ObitoForm()
	contexto = {'form': form}
	
	if DEBUG:
		print("** OBITOS ** ")
	
	#print("form: ", form)
	#print("#-------------------------------------------------")
		
	return render(request,'obitos.html',contexto)

	

#def home(request):
#	return render(request, 'home.html', {})

def home(request):
	first_name = "DCP"
	last_name = "Brasília-DF"
	return render(request,'home.html',{})

def about(request):
	first_name = "DCP"
	last_name = "Brasília-DF"
	return render(request,'about.html',{'first_name':first_name,'last_name':last_name})


def tabelasdcp(request):
	
	print ("** TABELASDCP-LISTA **")

	lista_tabelas =[]
	if request.method == 'POST':

		print ("** TABELASDCP-LISTA POST **")
		
		lista_registros=[]
		valores = dict(request.POST.items())
		for valor in valores.values():
			lista_registros.append(valor)

		print ("--postar_tabelas_indice(valor)--begin")
		item = postar_tabelas_indices(valor)
		print ("--postar_tabelas_indice(valor)--end")

		return render(request, 'tabelasdcp-lista.html', {'contexto': item})	
	
	else:		

		print ("** TABELASDCP-LISTA GET **")	

		tabelas = T21ListaTabelasDCP.objects.all()
		for i in range(tabelas.count()):
			lista_tabelas.append(tabelas.values()[i]['t21_nome_tabela'])
		
		return render(request,'tabelasdcp.html', {'tabelas':lista_tabelas})


def teste(request):
	return render(request,'sidenav.html',{})


def gratificacoes(request):
	first_name = "DCP"
	last_name = "Brasília-DF"
	return render(request,'gratificacoes.html',{})


def especificos(request):
	first_name = "DCP"
	last_name = "Brasília-DF"
	return render(request,'especificos.html',{})


def customizados(request):
	from src.testsoap import lista_servico, calcula_prazo, funcao1

	#first_name = "DCP"
	#last_name = "Brasília-DF"
	#prazo = calcula_prazo("41432","70362010","70292070")
	
	lista = lista_servico()
	#servico = resposta['cServicosCalculo']

	#listaservico ={'nome':'sobre','caldo':'212128','cep':21342309}
    
	return render(request,'customizados.html',{'num1':lista})





def lista(request):

	if request.method == "POST":
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request, ('Item adicionado à lista'))
			return render(request, 'lista.html', {'all_items':all_items})

	else:	
		all_items = List.objects.all
		return render(request, 'lista.html', {'all_items':all_items})


def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item removido da lista'))
	return redirect('lista')	

def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('lista')	

def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('lista')


def edit(request, list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)

		form = ListForm(request.POST or None, instance=item)
        
		if form.is_valid():
			form.save()
			messages.success(request, ('Item editado!'))
			return redirect('lista')

	else:
		item = List.objects.get(pk=list_id)
		return render(request, 'edit.html', {'item': item})



# outra forma de fazer 

#def about(request):
#	first_name = "Rangel"
#	last_name = "Cavalcante"
#	context  = {'first_name': first_name, 'last_name':last_name}
#	return render(request, "about.html", context)


# Create your views here.

