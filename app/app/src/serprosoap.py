from zeep import Client
import copy
from src.verificacpf import formater
from src.formatasoap import *
from acd_app.settings import TOKEN

#client = Client(wsdl='http://10.15.25.90:8080/SiapeSicapService?wsdl')
client = Client(wsdl ='https://app.sicap.agu.gov.br/SiapeSicapService?wsdl')
iu = ''
dados1=''
dados2=''


def buscarDataObito(lista_cpf_validos):
	#print ("#---(inicio)--buscarDataObito------------------------")
	#print ("#-lista_cpf_validos----------------------------------")
	#print (lista_cpf_validos)
	
	# todos os cpf válidos vêm numa lista, a lista_cpf_validos
	# vai ao servidor web com cada cpf válido e recebe de volta
	# o arquivo json

	# abre o arquivo json para retirar o nome, cpf e data de óbito	
	num_id = 0
	lista_de_obitos = []
	listavazia = {}
	
	# criar um dicionário com {'id':1,'{'cpf':cpf, 'nome':nome, 'data_obito':data_obito}, 'id':2, ....}

	dict_obitos = {}
	dict2 = {}
	new_dict ={}

	for cpf in lista_cpf_validos:
		#print("#-(cpf)--------------------------------------------")	
		#print(cpf)

		# busca no servidorweb a identificacao unica
		dados1 =client.service.pesquisarServidorCpf(cpf,TOKEN)
		if dados1 != None:
			iu = dados1['identificacaoUnica']
			nome = dados1['nome']
			cpf = formater(cpf)

		if dados1 != None:
			# com a iu buscar a data de obito
			dados2=client.service.getDataObitoServidor(iu,TOKEN)
			str_dados2 = str(dados2)
			#print('tam str_dados2',len(str_dados2))
			tdata=''
			
			if len(str_dados2) > 10:
				ano = str_dados2[0:4]
				mes = str_dados2[5:7]
				dia = str_dados2[8:10]
				tdata = dia + '/' + mes + "/" + ano
			
			#print('Data de obito:', dia, '/', mes,'/',ano)
			
			num_id = num_id + 1
			dict2['id'] = num_id
			dict2['cpf']= cpf
			dict2['nome'] = nome
			dict2['data'] = tdata
			new_dict = copy.deepcopy(dict2)
			dict_obitos[num_id] = new_dict 

			#print("#--dict_obitos-----------------------------------")	
			#print(dict_obitos)
			#print("#---(fim)--buscarDataObito---------------------------")

	return dict_obitos

def buscarFichaFinanceira(lista_cpf_validos,ano_inicial, ano_final):

	#print("# ====(INICIO)====(buscarFichaFinanceira)===============")

	num_id = 0
	lista_de_s = []
	listavazia = {}
	
	# criar um dicionário com {'id':1,'{'cpf':cpf, 'nome':nome, 'data_obito':data_obito}, 'id':2, ....}

	dict_fichas = {}
	dict2 = {}
	new_dict ={}
	dict_fichas2={}

	for cpf in lista_cpf_validos:
		#print("#-(cpf)--------------------------------------------")	
		#print(cpf)

		# busca no servidorweb a identificacao unica
		dados1 =client.service.pesquisarServidorCpf(cpf,TOKEN)
		
		if dados1 != None:
			dadosdoservidor = formataDadosServidor(dados1)
			
			if dadosdoservidor['iu'] != '':
				iu = dadosdoservidor['iu']
				nome = dadosdoservidor['nome']
				cpf = dadosdoservidor['cpf']

			# com a iu buscar a ficha financeira
			ficha = client.service.montarFichaFinanceiraServidor(iu,ano_inicial,ano_final,TOKEN)
			#print("dadosdoservidor:  \n")
			#print(dadosdoservidor)

			fichaformatada = formataFichaFinanceira(ficha)
			
			dict_fichas[iu]=fichaformatada
			
			#print ("Quantidade de registros(dict):",len(fichaformatada))
			#print("#--fichaformatada-------------------------------------")	
			#print (fichaformatada)

			#for i in range(len(fichaformatada['lancamentos'])):
			#	dict2 = fichaformatada['lancamentos'][i]
			#	new_dict = copy.deepcopy(dict2)
			#	dict_fichas[i]=new_dict

			#print("#--dict_fichas-----------------------------------")	
			#print(dict_fichas)
			#print("# ====(FIM)====(buscarFichaFinanceira)===============")


			#print("#--fichaformatada-----------------------------------")	
			#for i in dict_fichas2:
			#	print(i)
			#	print(dict_fichas2[i])
			#print(dict_fichas2)
			#print("# =======================")

	"""
	deve retornar um dicionário da seguinte forma:
			
	fichas={	IU1 : {'cadastro:{ dados_cadastro }, 'registros':{ lancamentos}},
				IU2 : {'cadastro:{ dados_cadastro }, 'registros':{ lancamentos}},
	 			...
	 			IUn : {'cadastro:{ dados_cadastro }, 'registros':{ lancamentos}
	 		}
	dados_cadastro={ {'iu':1234, 'nome':"joaquim", 
					   registros[{ 'ano':1992,
					   				'orgao':123,
					   				'matricula':123,
					   				'codgcargo':12,
					   				'codcargo':22, 
					   				'classe':'C', 
					   				'padrao': 'VI', 
					   				sigla: 'EST'}, {...},{...}
					   			]
	lancamentos=[
					[1992, 25000, 1, 1, 0, [0, 0, 0, 0, 0, 938364.73, 938364.73, 938364.73, 1126037.67, 2506028.98, 2506028.98, 2506028.98]], 
					[1992, 25000, 13, 1, 0, [0, 0, 0, 0, 0, 9383.64, 9383.64, 9383.64, 11260.37, 25060.28, 25060.28, 50120.57]], 
					[1992, 25000, 53, 1, 1, [0, 0, 0, 0, 0, 93836.47, 9383.64, 9383.64, 11260.37, 25060.28, 25060.28, 25060.28]], 
					[1992, 25000, 92, 1, 0, [0, 0, 0, 0, 0, 4044.39, 4044.36, 4044.36, 4853.52, 4853.22, 4853.22, 4853.22]], 
					[1992, 25000, 224, 1, 1, [0, 0, 0, 0, 0, 637866.04, 637866.04, 637866.04, 637866.04, 0, 0, 0]], 
					[1992, 25000, 591, 1, 0, [0, 0, 0, 0, 0, 0, 0, 0, 337811.3, 751808.69, 2004823.18, 2004823.18]],
				]	

	"""

	return dict_fichas


def lista_servico():
	servico = client.service.ListaServicos()
	
	lista = servico['cServicosCalculo']
	
	return lista

def calcula_prazo(codigo, cep_origem, cep_destino):

	# "41432","70362010","70292070"
	lista = {}
	prazo = client.service.CalcPrazo(codigo,cep_origem,cep_destino)
	
	resultado = prazo['cServico'][0]
	#lista = resultado

	return resultado





